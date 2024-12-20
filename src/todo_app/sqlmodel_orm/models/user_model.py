import re
from sqlmodel import SQLModel, Field, Relationship
from datetime import date
from typing import TYPE_CHECKING
from pydantic import EmailStr, field_validator

# Voorkom circulaire referentie, maar wel met type hinting in model naar foreign-key relatie tussen models
if TYPE_CHECKING:
    from todo_app.sqlmodel_orm.models.todo_model import Todo


class UserBase(SQLModel):
    email: EmailStr


class Users(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    password: str = Field()
    created_at: date | None = Field(default_factory=date.today)

    # Relationship to Todo
    todos: list["Todo"] = Relationship(back_populates="owner")


class UsersPublic(UserBase):
    id: int
    password: str


class UsersCreate(UserBase):
    email: EmailStr
    password: str

    @field_validator("password")
    def validate_password(cls, password):
        if not len(password) > 4:
            raise ValueError("Password must contain more than 4 characters")
        if not re.search(r'\d', password):
            raise ValueError("Password must contain at least one number.")
        return password


class UsersUpdate(SQLModel):
    password: str | None = None

