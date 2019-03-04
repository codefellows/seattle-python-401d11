from src import app

# can be a function
def test_functions():
    assert True


# can also be a class
class TestClass:
    @classmethod
    def setup_class(cls):
        print('setup_class')

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_tc1(self):
        pass

    def test_tc2(self):
        pass

    def test_home_route_get_status(self):
        """ tests / route status code"""
        rv = app.test_client().get('/')
        assert rv.status_code == 200
        assert b'<title>Home</title>' in rv.data

    def test_search_route_post_status(self, session):
        """ tests that /search post route gives correct status"""
        rv = app.test_client().post('/search', data={'zipcode': '98108'})
        assert rv.status_code == 302
    
    def test_search_route_post_status_again(self, session):
        """ tests that /search post route gives correct status"""
        rv = app.test_client().post('/search', data={'zipcode': '98108'}, follow_redirects=True)
        assert rv.status_code == 200