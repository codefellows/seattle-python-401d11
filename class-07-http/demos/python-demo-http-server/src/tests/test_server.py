import requests as req
import pytest


def test_server_get_home_route_status_200():
    response = req.get('http://127.0.0.1:5000/')
    assert response.status_code == 200

@pytest.mark.skip('pending')
def test_server_get_home_route_response_content():
    response = req.get('http://127.0.0.1:5000/')
    assert '<html><body><h1>hi!</h1></body></html>' in str(response.text)

@pytest.mark.skip('pending')
def test_server_get_with_querystring_test_route_status_200():
    response = req.get('http://127.0.0.1:5000/test?category=correct')
    assert response.status_code == 200

@pytest.mark.skip('pending')
def test_server_get_with_bad_querystring_test_route_status_200():
    response = req.get('http://127.0.0.1:5000/test?incorrect=querystring')
    assert response.status_code == 400

@pytest.mark.skip('pending')
def test_server_get_no_querystring_test_route_status_400():
    response = req.get('http://127.0.0.1:5000/test')
    assert response.status_code == 400

@pytest.mark.skip('pending')
def test_server_get_home_route_status_404():
    response = req.get('http://127.0.0.1:5000/failure')
    assert response.status_code == 404

@pytest.mark.skip('pending')
def test_server_head_home_route_status_302():
    response = req.head('http://127.0.0.1:5000/')
    assert response.status_code == 302

@pytest.mark.skip('pending')
def test_server_post_home_route_status_201():
    response = req.post('http://127.0.0.1:5000/')
    assert response.status_code == 201

@pytest.mark.skip('pending')
def test_server_post_home_route_response_content():
    response = req.post('http://127.0.0.1:5000/')
    assert '<html><body><h1>POST!</h1></body></html>' in str(response.text)

@pytest.mark.skip('pending')
def test_server_put_not_implemented_status_501():
    response = req.put('http://127.0.0.1:5000/')
    assert response.status_code == 501

@pytest.mark.skip('pending')
def test_server_delete_not_implemented_status_501():
    response = req.delete('http://127.0.0.1:5000/')
    assert response.status_code == 501
