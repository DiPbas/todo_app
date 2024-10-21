from fastapi import APIRouter
from fastapi import Query, HTTPException
from typing import List, Annotated
from sqlmodel import select

from ..sqlmodel_orm.models.user_model import Users, UsersCreate, UsersPublic, UsersUpdate
from ..dependencies import SessionDep

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UsersPublic)
def create_user(user: UsersCreate, session: SessionDep) -> Users:
    db_user = Users.model_validate(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@router.get("/", response_model=List[UsersPublic])
def read_users(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    users = session.exec(select(Users).offset(offset).limit(limit)).all()
    return users


@router.get("/{user_id}", response_model=UsersPublic)
def read_user(user_id: int, session: SessionDep):
    user = session.get(Users, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.patch("/{user_id}", response_model=UsersPublic)
def update_user(user_id: int, user: UsersUpdate, session: SessionDep):
    user_db = session.get(Users, user_id)
    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = user.model_dump(exclude_unset=True)
    user_db.sqlmodel_update(user_data)
    session.add(user_db)
    session.commit()
    session.refresh(user_db)
    return user_db


@router.delete("/{user_id}")
def delete_user(user_id: int, session: SessionDep):
    user = session.get(user, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    session.delete(user)
    session.commit()
    return {"ok": True}
