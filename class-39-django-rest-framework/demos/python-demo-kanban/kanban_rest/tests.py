from django.test import TestCase, RequestFactory
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate, APIRequestFactory
from board.models import Category, Card
from django.contrib.auth.models import User
from kanban_rest.views import CategoryListApiView
import json


class TestUserAPI(TestCase):
    def test_user_registration(self):
        user = {
            'username': 'test_user',
            'email': 'user@user.com',
            'password': 'test_pw'
        }
        response = self.client.post('/api/v1/register', user)
        self.assertIn(b'"username":"test_user"', response.content)

    def test_user_login(self):
        user = {
            'username': 'test_user',
            'email': 'user@user.com',
            'password': 'test_pw'
        }
        self.client.post('/api/v1/register', user)
        response = self.client.post('/api/v1/login', user)
        token = json.loads(response.content)

        self.assertEqual(len(token['token']), 40)

    def test_user_registration_status_code(self):
        user = {
            'username': 'test_user',
            'email': 'user@user.com',
            'password': 'test_pw'
        }
        response = self.client.post('/api/v1/register', user)
        self.assertEqual(response.status_code, 201)

    def test_user_login_status_code(self):
        user = {
            'username': 'test_user',
            'email': 'user@user.com',
            'password': 'test_pw'
        }
        self.client.post('/api/v1/register', user)
        response = self.client.post('/api/v1/login', user)
        self.assertEqual(response.status_code, 200)


class TestCategoryApi(APITestCase):

    def test_get_categories(self):

        ############# move into helper/factor when ready ###
        user = {
            'username': 'test_user',
            'email': 'user@user.com',
            'password': 'test_pw'
        }
        self.client.post('/api/v1/register', user)
        response = self.client.post('/api/v1/login', user)
        
        user = User.objects.get(username='test_user')
        #####################################################

        view = CategoryListApiView.as_view()

        # Make an authenticated request to the view...
        factory = APIRequestFactory()
        
        request = factory.get('/api/v1/category/')
        force_authenticate(request, user=user, token=user.auth_token)
        response = view(request)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(Category.objects.all()), 0)


class TestCardApi(TestCase):
    pass
