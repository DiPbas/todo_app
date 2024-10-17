from fastapi import APIRouter
from fastapi import FastAPI, Query, HTTPException
from typing import List, Annotated
from sqlmodel import select

from ..sqlmodel_orm.models.todo_model import *
from ..dependencies import SessionDep

router = APIRouter(
    prefix="/todos",
    tags=["todos"]
)

@router.get("/", response_model=List[Todo])
def read_todos(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
):
    todos = session.exec(select(Todo).offset(offset).limit(limit)).all()
    return todos