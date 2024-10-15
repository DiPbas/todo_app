from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from .database import engine
# Define Users model


class UserBase(SQLModel):
    email: str


class Users(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str = Field(default="wachtwoord")
    created_at: date | None = Field(default_factory=date.today)

    # Relationship to Todo
    todos: List["Todo"] = Relationship(back_populates="owner")


class UsersPublic(UserBase):
    id: int


class UsersCreate(UserBase):
    email: str


class UsersUpdate(UserBase):
    email: str | None = None
    hashed_password: str | None = None
    created_at: date | None = None

# Define Todo model


class TodoBase(SQLModel):
    date: date
    task: str
    done: Optional[bool] = False


class Todo(TodoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(foreign_key="users.id")

    # Relationship back to the user
    owner: Optional[Users] = Relationship(back_populates="todos")


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
