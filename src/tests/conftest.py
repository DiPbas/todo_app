import pytest
from fastapi.testclient import TestClient

from todo_app.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from testcontainers.postgres import PostgresContainer


# Fixture om de Postgres-container op te zetten en af te breken
@pytest.fixture(scope="session")
def postgres_db():
    # Start de PostgreSQL container met Testcontainers
    with PostgresContainer("postgres:latest") as postgres:
        # Stel de database URL in voor SQLAlchemy
        db_url = postgres.get_connection_url()

        # Maak de SQLAlchemy engine en sessie aan
        engine = create_engine(db_url)
        Session = sessionmaker(bind=engine)

        # Creëer de database tabellen
        SQLModel.metadata.create_all(engine)

        yield Session, engine

        # Na de testomgeving, drop de tabellen
        SQLModel.metadata.drop_all(engine)


@pytest.fixture(scope="session")
def test_api():
    client = TestClient(app)
    yield client

    client.close()
