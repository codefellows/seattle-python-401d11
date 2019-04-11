from django.test import TestCase, RequestFactory


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
        import json
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


class TestCategoryApi(TestCase):
    pass


class TestCardApi(TestCase):
    pass
