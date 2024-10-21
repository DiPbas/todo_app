from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from typing import TYPE_CHECKING


# Voorkom circulaire referentie, maar wel met type hinting in model naar foreign-key relatie tussen models
if TYPE_CHECKING:
    from .todo_model import Todo


class UserBase(SQLModel):
    email: str


class Users(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    hashed_password: str = Field(default="wachtwoord")
    created_at: date | None = Field(default_factory=date.today)

    # Relationship to Todo
    todos: list["Todo"] = Relationship(back_populates="owner")


class UsersPublic(UserBase):
    id: int


class UsersCreate(UserBase):
    email: str


class UsersUpdate(UserBase):
    email: str | None = None
    hashed_password: str | None = None
    created_at: date | None = None
