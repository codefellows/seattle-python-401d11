def test_get_home(app):
    rv = app.test_client().get('/')
    assert b'<h1>Welcome to the site</h1>' in rv.data

def test_search_santa_cruz_zip_status(app):
    rv = app.test_client().post('/search', data={'zipcode':'95062'})
    
    assert rv.status_code == 302

def test_search_santa_cruz_zip(app):
    rv = app.test_client().post('/search', data={'zipcode':'95062'}, follow_redirects=True)
    
    assert b'<h2>Search for cities</h2>' not in rv.data

    assert rv.status_code == 200
