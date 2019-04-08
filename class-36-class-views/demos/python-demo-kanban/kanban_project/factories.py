import factory
from django.contrib.auth.models import User
from board.models import Card, Category


class UserFactory(factory.django.DjangoModelFactory):
    """Create a test user for writing tests."""

    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class CategoryFactory(factory.django.DjangoModelFactory):
    """Create a test category for writing tests."""

    class Meta:
        model = Category

    user = factory.SubFactory(UserFactory)
    name = factory.Faker('word')
    description = factory.Faker('paragraph')


class CardFactory(factory.django.DjangoModelFactory):
    """Create a test card for writing tests."""

    class Meta:
        model = Card

    assigned_to = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
    title = factory.Faker('word')
    description = factory.Faker('paragraph')
