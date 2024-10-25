import pytest

from todo_app.tests.factories.users_factory import UserFactory


@pytest.fixture(scope="session")
def setup_db(postgres_db):
    # Fixture om de sessie op te zetten
    Session, engine = postgres_db
    # Zorg dat de factory de juiste sessie gebruikt
    UserFactory._meta.sqlalchemy_session = Session()

    yield Session()

    # Sluit de sessie na elke test af
    UserFactory._meta.sqlalchemy_session.close()
    engine.dispose()  # Sluit de database connecties af


@pytest.fixture(scope="f")
def setup_api(test_api):
    client = test_api

    yield client

    client.close()


def test_password_isEcrypted_after_create(setup_api, setup_db):
    # Arrange
    user = UserFactory()

    pay_load = {"email": user.email, "password": user.password}

    # Act
    response = setup_api.post("/users/", json=pay_load)

    # Assert
    assert user.password != response.json().get("password")
