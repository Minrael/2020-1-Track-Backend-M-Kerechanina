import factory
from user.models import User

class RandomUserFactory(factory.Factory):
    class Meta:
        model = User

    username=factory.Faker('first_name')