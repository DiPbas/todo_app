import pytest

from tests.setup.factories.users_factory import UserFactory


@pytest.fixture(scope="session", autouse=True)
def setup_db(postgres_db):
    # Fixture om de sessie op te zetten
    Session, engine = postgres_db
    
    UserFactory._meta.sqlalchemy_session = Session()

    yield Session()

    UserFactory._meta.sqlalchemy_session.close()
    engine.dispose()


def test_password_isEcrypted_after_create(test_api):
    # Arrange
    user = UserFactory()

    pay_load = {"email": user.email, "password": user.password}

    # Act
    response = test_api.post("/users/", json=pay_load)

    # Assert
    assert user.password != response.json().get("password")
