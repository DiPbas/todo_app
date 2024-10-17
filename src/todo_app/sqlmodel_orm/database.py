from sqlalchemy.ext.declarative import declarative_base
from sqlmodel import create_engine

SQLALCHEMY_DATABASE_URL = "postgresql://bas:bas@localhost:5432/todo_db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)


Base = declarative_base()
