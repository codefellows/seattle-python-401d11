import factory
from django.contrib.auth.models import User
from budgets_app.models import Budget, Transaction


class UserFactory(factory.django.DjangoModelFactory):
    """ Create test User
    """
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')


class BudgetFactory(factory.django.DjangoModelFactory):
    """ Create test Budget
    """
    class Meta:
        model = Budget

    name = factory.Faker('word')
    user = factory.SubFactory(UserFactory)
    total_budget = factory.Faker('random_int')


class TransactionFactory(factory.django.DjangoModelFactory):
    """ Create test Transaction
    """
    class Meta:
        model = Transaction

    description = factory.Faker('paragraph')
    budget = factory.SubFactory(BudgetFactory)
    type = factory.Faker('word')
    amount = factory.Faker('random_int')
