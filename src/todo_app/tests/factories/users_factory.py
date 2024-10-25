import factory
import random

import factory.fuzzy
from todo_app.sqlmodel_orm.models.user_model import Users


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Users  # SQLAlchemy model
        sqlalchemy_session = None  # Dit wordt later ingesteld
        sqlalchemy_session_persistence = "commit"

    email = factory.Faker("email")
    password = "test"
    # hashed_password = factory.LazyFunction(
    #    lambda: hash_password(UserTestConstants.USER_DEFAULT_PASSWORD)
    # )
    created_at = factory.Faker("date_this_decade")
    id = factory.LazyAttribute(lambda x: random.randrange(0, 10000))
    todos = []
