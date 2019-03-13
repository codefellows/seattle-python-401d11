class TestBaseRoutes:
    """
    """
    def test_home_route_status(self, client):
        """
        uses client fixture
        """
        res = client.get('/')
        assert res.status_code == 200

    def test_home_route_title(self, client):
        """
        """
        res = client.get('/')
        assert b'<title>home</title>' in res.data

    def test_unknown_route_status(self, client):
        """
        """
        res = client.get('/does_not_exist')
        assert res.status_code == 404
        assert b'<h1>404 - Page Not Found</h1>' in res.data