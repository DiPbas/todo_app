from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship
from datetime import date

from ..database import engine
from .user_model import Users


class TodoBase(SQLModel):
    date: date
    task: str
    done: Optional[bool] = False


class Todo(TodoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(foreign_key="users.id")

    # Relationship back to the user
    owner: Optional["Users"] = Relationship(back_populates="todos")


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
