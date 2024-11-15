from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select
from typing import Annotated

from todo_app.sqlmodel_orm.models.todo_model import Todo, TodoCreate, TodoRead, TodoUpdate
from todo_app.dependencies import SessionDep
from todo_app.sqlmodel_orm.models.user_model import Users
from todo_app.internal.exceptions import NotFoundError

router = APIRouter(prefix="/todos", tags=["todos"])


@router.post("/", response_model=TodoRead)
def create_todo(todo: TodoCreate, session: SessionDep) -> Todo:
    user = session.get(Users, todo.user_id)
    if not user:
        raise NotFoundError(detail=f"User with id: {todo.user_id} not found")

    db_todo = Todo.model_validate(todo)
    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo


@router.get("/", response_model=list[TodoRead])
def read_todos(
    session: SessionDep,
    user_id: int | None = None,
    offset: Annotated[
        int, Query(ge=0)
    ] = 0,  # Via Annotated en Query maak je extra validatie mogelijk over de parameters
    limit: Annotated[int, Query(le=100)] = 100,
):
    query = select(Todo)
    if user_id is not None:
        query = query.where(Todo.user_id == user_id)

    todos = session.exec(query.offset(offset).limit(limit)).all()
    return todos


@router.get("/{todo_id}", response_model=TodoRead)
def read_todo(todo_id: int, session: SessionDep):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise NotFoundError(detail=f"TODO List with id: {todo_id} not found")
    return todo


@router.patch("/{todo_id}", response_model=TodoRead)
def update_todo(todo_id: int, todo: TodoUpdate, session: SessionDep):
    db_todo = session.get(Todo, todo_id)
    if not db_todo:
        raise NotFoundError(detail=f"TODO List with id: {todo_id} not found")

    todo_data = todo.model_dump(exclude_unset=True)
    db_todo.sqlmodel_update(todo_data)

    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)
    return db_todo


@router.delete("/{todo_id}")
def delete_todo(todo_id: int, session: SessionDep):
    todo = session.get(Todo, todo_id)
    if not todo:
        raise NotFoundError(detail=f"TODO List with id: {todo_id} not found")

    session.delete(todo)
    session.commit()
    return {"ok": True}
