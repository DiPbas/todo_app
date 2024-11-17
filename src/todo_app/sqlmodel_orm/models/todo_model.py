from sqlmodel import SQLModel, Field, Relationship
from datetime import (
    date as date_dtype,
)  # change name date because field is also named date

from todo_app.sqlmodel_orm.database import engine
from todo_app.sqlmodel_orm.models.user_model import Users
from todo_app.sqlmodel_orm.models.base_model_metadata import BaseModel 

class TodoBase(BaseModel):
    task: str
    done: bool | None = False


class Todo(TodoBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int | None = Field(foreign_key="users.id")
    date: date_dtype | None = Field(default_factory=date_dtype.today)
    # Relationship back to the user
    owner: Users | None = Relationship(back_populates="todos")


class TodoCreate(TodoBase):
    user_id: int  # User ID required to link the todo to a user


class TodoRead(TodoBase):
    id: int
    user_id: int


class TodoUpdate(TodoBase):
    date: date_dtype | None = None
    task: str | None = None
    done: bool | None = None


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
