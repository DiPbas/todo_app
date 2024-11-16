from fastapi import APIRouter
from fastapi import Query
from typing import List, Annotated
from sqlmodel import select
from todo_app.sqlmodel_orm.models.user_model import (
    Users,
    UsersCreate,
    UsersPublic,
    UsersUpdate,
)
from todo_app.dependencies import SessionDep
from todo_app.internal.encrypt import hash_password
from todo_app.internal.helper import entity_exists

router = APIRouter(prefix="/users", tags=["users"])



@router.post("/", response_model=UsersPublic)
def create_user(user: UsersCreate, session: SessionDep):
    user.password  =  hash_password(user.password)
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
    user = entity_exists(entity_id=user_id,model=Users, session=session)
    return user


@router.patch("/{user_id}", response_model=UsersPublic)
def update_user(user_id: int, user_update: UsersUpdate, session: SessionDep):
    user = entity_exists(entity_id=user_id,model=Users, session=session)

    update_data = user_update.model_dump(exclude_unset=True)
    user.sqlmodel_update(update_data)
    
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@router.delete("/{user_id}")
def delete_user(user_id: int, session: SessionDep):
    user = entity_exists(entity_id=user_id,model=Users, session=session)
    session.delete(user)
    session.commit()
    return {"ok": True}

