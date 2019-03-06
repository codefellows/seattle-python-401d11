def test_home(app):
    rv = app.test_client().get('/')
    assert rv.status_code == 200



