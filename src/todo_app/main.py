from fastapi import FastAPI, Query, HTTPException
from typing import List, Annotated
from sqlmodel import select
from .sqlmodel_orm.models import *
from .dependencies import SessionDep

app = FastAPI()


@app.post("/users/", response_model=UsersPublic)
def create_user(user: UsersCreate, session: SessionDep) -> Users:
    db_user = Users.model_validate(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@app.get("/users/", response_model=List[UsersPublic])
def read_users(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    users = session.exec(select(Users).offset(offset).limit(limit)).all()
    return users


@app.get("/users/{user_id}", response_model=UsersPublic)
def read_user(user_id: int, session: SessionDep):
    user = session.get(Users, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.patch("/users/{user_id}", response_model=UsersPublic)
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


@app.delete("/users/{user_id}")
def delete_user(user_id: int, session: SessionDep):
    user = session.get(user, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    session.delete(user)
    session.commit()
    return {"ok": True}
