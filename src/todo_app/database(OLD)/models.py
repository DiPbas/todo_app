from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Date,
    ForeignKey,
    TIMESTAMP,
    func,
)
from sqlalchemy.orm import relationship

from .database import Base

# Users model


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False)
    # Vergeet niet om dit NOT NULL te maken
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    # Relation to Todo model
    todos = relationship("Todo", back_populates="owner", cascade="all, delete-orphan")


# Todos model


class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    date = Column(Date, nullable=False)
    task = Column(String(255), nullable=False)
    done = Column(Boolean, default=False)

    # Relationship back to the user
    owner = relationship("Users", back_populates="todos")
