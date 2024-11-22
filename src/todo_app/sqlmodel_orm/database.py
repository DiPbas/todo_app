from sqlalchemy.ext.declarative import declarative_base
from sqlmodel import create_engine
from todo_app.sqlmodel_orm.models.base_model_metadata import BaseModel

SQLALCHEMY_DATABASE_URL = "postgresql://bas:bas@postgres_db:5432/todo_db"
#SQLALCHEMY_DATABASE_URL = "postgresql://bas:bas@localhost:5432/todo_db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)


Base = declarative_base()
