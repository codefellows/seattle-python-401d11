from django.test import TestCase
from budget_tool_project.factories import UserFactory, BudgetFactory, TransactionFactory


class TestBudgetModels(TestCase):
    def setUp(self):
        self.budget = BudgetFactory(
            name='Red Bull',
            total_budget=234.56
        )

    def test_default_budget_attrs(self):
        self.assertEqual(self.budget.name, 'Red Bull')
        self.assertEqual(self.budget.total_budget, 234.56)


class TestTransactionModels(TestCase):
    def setUp(self):
        self.budget = BudgetFactory(
            name='food',
            total_budget=234.56
        )
        self.transaction = TransactionFactory(
            description='apples',
            type='withdrawal',
            amount=1.23,
            budget=self.budget
        )

    def test_default_budget_attrs(self):
        self.assertEqual(self.transaction.description, 'apples')
        self.assertEqual(self.transaction.amount, 1.23)
        self.assertEqual(self.transaction.budget.name, 'food')
