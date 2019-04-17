from django.test import TestCase, Client
from django.template.loader import render_to_string

from budget_tool_project.factories import (
    BudgetFactory, TransactionFactory, UserFactory,
    Budget, Transaction
)


class TestBudgetViews(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('12345')
        self.user.save()
        self.c = Client()

    def test_denied_if_no_login(self):
        res = self.c.get('/budgets', follow=True)
        self.assertEqual(res.status_code, 200)

        with self.assertTemplateUsed('registration/login.html'):
            render_to_string('registration/login.html')

    def test_view_budgets_when_logged_in(self):
        self.c.login(
            username=self.user.username,
            password='12345'
        )
        budgets = BudgetFactory(user=self.user)
        res = self.c.get('/budgets', follow=True)
        self.assertIn(budgets.name.encode(), res.content)

    def test_lists_only_owned_budgets(self):
        self.c.login(
            username=self.user.username,
            password='12345'
        )
        own_budgets = BudgetFactory(user=self.user)
        other_budgets = BudgetFactory()
        res = self.c.get('/budgets', follow=True)
        self.assertIn(own_budgets.name.encode(), res.content)
        self.assertNotIn(other_budgets.name.encode(), res.content)


class TestTransactionViews(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.user.set_password('12345')
        self.user.save()
        self.budget = BudgetFactory(user=self.user)
        self.c = Client()

    def test_denied_if_no_login(self):
        res = self.c.get('/budgets/' + str(self.budget.id), follow=True)
        self.assertEqual(res.status_code, 200)

        with self.assertTemplateUsed('registration/login.html'):
            render_to_string('registration/login.html')

    def test_view_transactions_when_logged_in(self):
        self.c.login(
            username=self.user.username,
            password='12345'
        )
        transactions = TransactionFactory(budget=self.budget)
        res = self.c.get('/budgets/' + str(self.budget.id), follow=True)
        self.assertIn(transactions.description.encode(), res.content)
