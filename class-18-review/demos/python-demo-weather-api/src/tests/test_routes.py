class TestAuthentication:
    """
    """
    def test_registration_page_status(self, client):
        """
        """
        res = client.get('/register')
        assert res.status_code == 200

    def test_registration_body(self, client):
        """
        """
        res = client.get('/register')
        assert b'Register' in res.data

    def test_registration_redirect_status(self, client):
        """
        """
        res = client.post(
            '/register',
            data={'email': 'test@example.com', 'password': 'seekret'},
            follow_redirects=True,
        )
        assert res.status_code == 200

    def test_registration_redirect_to_login(self, client):
        """
        """
        res = client.post(
            '/register',
            data={'email': 'test@example.com', 'password': 'seekret'},
            follow_redirects=True,
        )
        assert b'<title>Login</title>' in res.data

    def test_registered_user_can_login(self, client):
        """
        """
        client.post(
            '/register',
            data={'email': 'test@example.com', 'password': 'seekret'},
            follow_redirects=True,
        )
        res = client.post(
            '/login',
            data={'email': 'test@example.com', 'password': 'seekret'},
            follow_redirects=True,
        )
        assert res.status_code == 200
        assert b'<title>Weather</title>' in res.data
        # assert check_title('Weather', res)

    def test_register_invalid_inputs(self, client):
        """
        """
        res = client.post(
            '/register',
            follow_redirects=True,
        )
        assert b'Register' in res.data

    def test_login_page_status(self, client):
        """
        """
        res = client.get('/login')
        assert res.status_code == 200

    def test_login_page_res_body(self, client):
        """
        """
        res = client.get('/login')
        assert b'Login' in res.data

    def test_login_page_redirect_status(self, client, user):
        """
        """
        res = client.post(
            '/login',
            data={'email': user.email, 'password': 'secret'},
            follow_redirects=True,
        )
        assert res.status_code == 200

    def test_login_page_redirect_to_weather_detail(self, client, user, city):
        """
        """
        res = client.post(
            '/login',
            data={'email': user.email, 'password': 'secret'},
            follow_redirects=True,
        )
        expected = f'{city.name}'
        assert expected.encode() in res.data

    def test_login_invalid_inputs(self, client):
        """
        """
        res = client.post(
            '/login',
            follow_redirects=True,
        )
        assert b'Login' in res.data

    def test_logout_redirect_status(self, authenticated_client):
        """
        """
        res = authenticated_client.get('/logout', follow_redirects=True)
        assert res.status_code == 200

    def test_logout_unauthenticated(self, client):
        """
        """
        res = client.get('/logout')
        assert res.status_code == 404


class TestAuthenticatedRoutes:
    """
    """
    def test_search_route_status(self, authenticated_client):
        """
        """
        res = authenticated_client.get('/search')
        assert res.status_code == 200

    def test_search_route_status_unauthenticated(self, client):
        """
        """
        res = client.get('/search')
        assert res.status_code == 404

    def test_search_route_no_categories(self, authenticated_client):
        """
        """
        res = authenticated_client.get('/search')
        assert b'Please create a Category' in res.data

    def test_search_route_with_categories(self, authenticated_client, category):
        """
        """
        res = authenticated_client.get('/search')
        assert b'action="/search"' in res.data
        assert b'zipcode' in res.data


