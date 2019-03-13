"""
This module uses test functions vs.
TestClass with methods
This is purely to show the different styles
"""

import pytest


def test_get_register_status(client):
    res = client.get('/register')
    assert res.status_code == 200


def test_get_register_has_correct_title(client):
    res = client.get('/register')
    assert b'<title>Register</title>' in res.data


def test_has_correct_nav_when_not_logged_in(client):
    res = client.get('/')
    assert b'<a href="/"' in res.data
    assert b'<a href="/register"' in res.data
    assert b'<a href="/login"' in res.data
    assert b'<a href="/logout"' not in res.data


def test_has_correct_nav_when_logged_in(authenticated_client):
    res = authenticated_client.get('/')
    assert b'<a href="/"' in res.data
    assert b'<a href="/register"' not in res.data
    assert b'<a href="/login"' not in res.data
    assert b'<a href="/logout"' in res.data


def test_register_post(client):
    credentials = {'email': 'foo@bar.baz', 'password': ' foobarbaz'}
    res = client.post('/register', data=credentials, follow_redirects=True)
    res = client.post('/register', data=credentials, follow_redirects=True)
    assert b'foo@bar.baz has already been registered.' in res.data
    assert b'<title>Register</title>' in res.data
    

def test_get_login_status(client):
    res = client.get('/login')
    assert res.status_code == 200


def test_get_login_has_correct_title(client):
    res = client.get('/login')
    assert b'<title>Login</title>' in res.data


def test_post_successful_login_page_status(authenticated_client):
    res = authenticated_client.get('/login')
    assert res.status_code == 200


def test_post_successful_login_page_title(authenticated_client):
    res = authenticated_client.get('/login')
    assert b'<title>Login</title>' in res.data
    

def test_logout(authenticated_client):
    res = authenticated_client.get('/logout', follow_redirects=True)
    assert res.status_code == 200
    assert b'<title>Login</title>' in res.data

def test_not_logged_in_protected_route(client):
    res = client.get('/weather')
    assert res.status_code == 404
