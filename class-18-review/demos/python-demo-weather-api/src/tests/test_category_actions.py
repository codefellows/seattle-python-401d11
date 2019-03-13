from ..models import Category

def test_create_category(authenticated_client):
    data = {'name': 'pasta'}
    res = authenticated_client.post('/weather', data=data, follow_redirects=True)
    assert res.status_code == 200
    assert b'<title>Search</title>' in res.data
    categories = Category.query.all()
    assert len(categories) == 1

def test_category_count_again(authenticated_client):
    data = {'name': 'nuts'}
    res = authenticated_client.post('/weather', data=data, follow_redirects=True)
    assert res.status_code == 200
    assert b'<title>Search</title>' in res.data
    categories = Category.query.all()
    assert len(categories) == 1

def test_category_count_again(authenticated_client):
    data = {'name': 'nuts'}
    res = authenticated_client.post('/weather', data=data, follow_redirects=True)
    nuts = Category.query.first()
    assert nuts.user.email == 'default@example.com'
    assert len(nuts.cities) == 0




