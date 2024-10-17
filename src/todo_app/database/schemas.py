from pydantic import BaseModel, EmailStr
from datetime import date
from typing import List, Optional


class TodoBase(BaseModel):
    date: date
    task: str
    done: Optional[bool] = False

    class Config:
        orm_mode = True


class TodoCreate(TodoBase):
    pass  # Geen id, omdat het automatisch wordt aangemaakt door de database


class Todo(TodoBase):
    id: int
    user_id: int


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class Users(UserBase):
    id: int
    todos: List[Todo] = []  # Verander 'items' naar 'todos'

    class Config:
        orm_mode = True
