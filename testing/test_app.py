import pytest
import json
from app import app

def test_web_root():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Web App with Python Flask!'

def test_web_data():
    response = app.test_client().get('/data')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hello here is my data!'

def test_web_home():
    response = app.test_client().get('/home')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hello here is my Home folder!'

def test_web_init():
    response = app.test_client().get('/init')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hello here is my init web page!'
    
@pytest.mark.get_request
def test_get_all_books():
    response = app.test_client().get('/bookapi/books')

    res = json.loads(response.data.decode('utf-8')).get("Books")
    assert type(res[0]) is dict
    assert type(res[1]) is dict
    assert res[0]['author'] == 'Havard'
    assert res[1]['author'] == 'Will'
    assert response.status_code == 200
    assert type(res) is list


@pytest.mark.get_request
def test_get_book_by_id():
    response = app.test_client().get('/bookapi/books/1')
    res = json.loads(response.data.decode('utf-8')).get("Book")
    print(res)
    assert res['id'] == 1
    assert res['author'] == 'Havard'
    assert res['title'] == 'CS50'
    assert response.status_code == 200