from django.test import TestCase, RequestFactory
from rest_framework.test import APITestCase, force_authenticate, APIRequestFactory
from budget_tool_project.factories import (
    UserFactory, BudgetFactory, TransactionFactory)
from budgets_app.models import Budget, Transaction, User


class TestUserAPI(APITestCase):
    def test_user_register_login(self):
        user = {
            'username': 'tester',
            'email': 'test@test.com',
            'password': '12345'
        }
        register_res = self.client.post(
            '/api/v1/register', user, format='json')
        self.assertEqual(register_res.status_code, 201)
        user_res = self.client.get(
            '/api/v1/user/' + str(register_res.data['id']))
        self.assertEqual(user_res.data['username'], 'tester')
        login_res = self.client.post('/api/v1/login', user)
        self.assertEqual(login_res.status_code, 200)
        self.assertTrue(len(login_res.data['token']) > 30)


class TestBudgetAPI(APITestCase):
    def setUp(self):
        user = {
            'username': 'test_user',
            'email': 'user@user.com',
            'password': 'test_pw'
        }
        self.client.post('/api/v1/register', user)
        response = self.client.post('/api/v1/login', user)
        self.user = User.objects.get(username='test_user')

    def test_not_logged_in(self):
        res = self.client.get('/api/v1/budgets')
        self.assertEqual(res.status_code, 401)

    def test_logged_in(self):
        self.client.force_authenticate(user=self.user)
        res = self.client.get('/api/v1/budgets')
        self.assertEqual(res.status_code, 200)

    def test_create_budget(self):
        budget = {
            'name': 'red bull',
            'total_budget': '200'
        }
        self.client.force_authenticate(user=self.user)
        res = self.client.post('/api/v1/budgets', budget, format='json')
        self.assertEqual(res.data['name'], 'red bull')
        saved_budget = Budget.objects.get(name=res.data['name'])
        self.assertTrue(saved_budget.name == 'red bull')

    def test_return_budgets(self):
        budget = {
            'name': 'red bull',
            'total_budget': '200'
        }
        self.client.force_authenticate(user=self.user)
        self.client.post('/api/v1/budgets', budget, format='json')
        res = self.client.get('/api/v1/budgets')
        self.assertTrue(res.data[0]['name'] == 'red bull')

    def test_get_budget_detail(self):
        budget = {
            'name': 'red bull',
            'total_budget': '200'
        }
        self.client.force_authenticate(user=self.user)
        res1 = self.client.post('/api/v1/budgets', budget, format='json')
        res2 = self.client.get('/api/v1/budgets/' + str(res1.data['id']))
        self.assertTrue(res2.data['name'] == 'red bull')


class TestTransactionAPI(APITestCase):
    def setUp(self):
        user = {
            'username': 'test_user',
            'email': 'user@user.com',
            'password': 'test_pw'
        }
        self.client.post('/api/v1/register', user)
        response = self.client.post('/api/v1/login', user)
        self.user = User.objects.get(username='test_user')

        budget = {
            'name': 'food',
            'total_budget': '600'
        }
        self.client.force_authenticate(user=self.user)
        self.client.post('/api/v1/budgets', budget, format='json')
        self.budget = Budget.objects.get(name='food')

    def test_logged_in(self):
        res = self.client.get('/api/v1/transactions')
        self.assertEqual(res.status_code, 200)

    def test_create_transaction(self):
        transaction = {
            'description': 'bananas',
            'type': 'withdrawal',
            'amount': 5,
            'budget_name': self.budget.name
        }
        res = self.client.post('/api/v1/transactions',
                               transaction, format='json')

    def test_return_transactions(self):
        transaction = {
            'description': 'bananas',
            'type': 'withdrawal',
            'amount': 5,
            'budget_name': self.budget.name
        }
        self.client.post('/api/v1/transactions', transaction, format='json')
        res = self.client.get('/api/v1/transactions')
        self.assertTrue(res.data[0]['description'] == 'bananas')

    def test_get_transaction_detail(self):
        transaction = {
            'description': 'bananas',
            'type': 'withdrawal',
            'amount': 5,
            'budget_name': self.budget.name
        }
        res1 = self.client.post('/api/v1/transactions', transaction, format='json')
        res2 = self.client.get('/api/v1/transactions/' + str(res1.data['id']))
        self.assertTrue(res2.data['description'] == 'bananas')
