from typing import Optional
from sqlmodel import Session, select
from .models import Users, Todo
# from passlib.context import CryptContext

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Password utilities


def get_password_hash(password: str) -> str:
    return password + "geheim"

# Get a user by id


def get_user(db: Session, user_id: int) -> Optional[Users]:
    return db.get(Users, user_id)

# Get a user by email


def get_user_by_email(db: Session, email: str) -> Optional[Users]:
    statement = select(Users).where(Users.email == email)
    return db.exec(statement).first()

# Create a new user


def create_user(db: Session, user: Users) -> Users:
    user.hashed_password = get_password_hash(user.hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Get all todos


def get_todos(db: Session, skip: int = 0, limit: int = 100) -> list[Todo]:
    statement = select(Todo).offset(skip).limit(limit)
    return db.exec(statement).all()

# Create a new todo


def create_user_todo(db: Session, todo: Todo, user_id: int) -> Todo:
    todo.user_id = user_id
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo
