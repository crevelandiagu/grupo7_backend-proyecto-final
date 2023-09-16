from app import app
import json
from faker import Faker
from unittest.mock import patch
from faker.generator import random

fake_data = Faker()

'''----------- Test ping --------------------'''
def test_ping():
    response = app.test_client().get('/app_performance/ping')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'pong'


'''----------- Test create offer success --------------------'''

@patch('payments.views.get_token')
def test_create_offer_201(mock_token):
    data = 	{
        "postId":fake_data.random_int(1,10),
        "description": fake_data.word(),
        "size": random.choice(["SMALL", "MEDIUM", "LARGE"]),
        "fragile": random.choice([True, False]),
        "offer": fake_data.random_int(100,1000)
    }
    token="abcdefg"

    mock_token.return_value = {"user_id": fake_data.random_int(1,10)}, 200
    response = app.test_client().post('/app_performance', json=data, headers={"Authorization": f'Bearer {token}'})
    response_info= json.loads(response.data.decode('utf-8'))
    assert response.status_code == 201
    assert response_info['offer']== str(data['offer'])
    assert len(list(response_info.keys())) == 8

'''----------- Test create offer unauthorized --------------------'''

@patch('payments.views.get_token')
def test_create_offer_401(mock_token):
    data = 	{
        "postId":fake_data.random_int(1,10),
        "description": fake_data.word(),
        "size": random.choice(["SMALL", "MEDIUM", "LARGE"]),
        "fragile": random.choice([True, False]),
        "offer": fake_data.random_int(100,1000)
    }
    token="abcdefg"

    mock_token.return_value = "Invalid token", 401
    response = app.test_client().post('/app_performance', json=data, headers={"Authorization": f'Bearer {token}'})
    assert response.status_code == 401

'''----------- Test create offer invalid values --------------------'''

@patch('payments.views.get_token')
def test_create_offer_400_invalid(mock_token):
    data = 	{
        "postId":fake_data.word(),
        "description": fake_data.word(),
        "size": random.choice(["SMALL", "MEDIUM", "LARGE"]),
        "fragile": random.choice([True, False]),
        "offer": fake_data.random_int(100,1000)
    }
    token="abcdefg"

    mock_token.return_value = {"user_id": fake_data.random_int(1,10)}, 200
    response = app.test_client().post('/app_performance', json=data, headers={"Authorization": f'Bearer {token}'})
    assert response.status_code == 412

'''----------- Test create offer missing values --------------------'''

@patch('payments.views.get_token')
def test_create_offer_400_missing(mock_token):
    data = 	{
        "postId":fake_data.random_int(1,100),
        "description": fake_data.word(),
        "fragile": random.choice([True, False]),
        "offer": fake_data.random_int(100,1000)
    }
    token="abcdefg"

    mock_token.return_value = {"user_id": fake_data.random_int(1,10)}, 200
    response = app.test_client().post('/app_performance', json=data, headers={"Authorization": f'Bearer {token}'})
    assert response.status_code == 400

'''----------- Test get app_performance success --------------------'''

@patch('payments.views.get_token')
def test_get_offers_200(mock_token):
    data = 	{
        "postId":fake_data.random_int(1,10),
        "description": fake_data.word(),
        "size": random.choice(["SMALL", "MEDIUM", "LARGE"]),
        "fragile": random.choice([True, False]),
        "offer": fake_data.random_int(100,1000)
    }
    token="abcdefg"

    mock_token.return_value = {"user_id": fake_data.random_int(1,10)}, 200
    response = app.test_client().post('/app_performance', json=data, headers={"Authorization": f'Bearer {token}'})
    response_info= json.loads(response.data.decode('utf-8'))
    assert response.status_code == 201
    offer_id = response_info['id']

    response = app.test_client().get('/app_performance', headers={"Authorization": f'Bearer {token}'})
    response_info= json.loads(response.data.decode('utf-8'))
    assert response.status_code == 200
    ids = [i['id'] for i in response_info]
    assert offer_id in ids

'''----------- Test get app_performance unauthorized --------------------'''

@patch('payments.views.get_token')
def test_get_offers_401(mock_token):
    token="abcdefg"
    mock_token.return_value = "Invalid token", 401
    response = app.test_client().get('/app_performance', headers={"Authorization": f'Bearer {token}'})
    assert response.status_code == 401

'''----------- Test get app_performance ivalid values --------------------'''
@patch('payments.views.get_token')
def test_get_offers_400(mock_token):
    token="abcdefg"
    mock_token.return_value = {"user_id": 1}, 200
    response = app.test_client().get('/app_performance?post=a', headers={"Authorization": f'Bearer {token}'})
    assert response.status_code == 400

'''----------- Test get app_performance parameters success --------------------'''

@patch('payments.views.get_token')
def test_get_offers_200_parameters(mock_token):
    data = 	{
        "postId":10001,
        "description": fake_data.word(),
        "size": random.choice(["SMALL", "MEDIUM", "LARGE"]),
        "fragile": random.choice([True, False]),
        "offer": fake_data.random_int(100,1000)
    }
    token="abcdefg"

    mock_token.return_value = {"user_id": 1}, 200
    response = app.test_client().post('/app_performance', json=data, headers={"Authorization": f'Bearer {token}'})
    response_info= json.loads(response.data.decode('utf-8'))
    assert response.status_code == 201
    offer_id = response_info['id']

    response = app.test_client().get('/app_performance?post=10001&filter=me', headers={"Authorization": f'Bearer {token}'})
    response_info= json.loads(response.data.decode('utf-8'))
    assert response.status_code == 200
    ids = [i['id'] for i in response_info]
    assert offer_id in ids

'''----------- Test get offer success --------------------'''

@patch('payments.views.get_token')
def test_get_offer_200_parameters(mock_token):
    data = 	{
        "postId":fake_data.random_int(100,1000),
        "description": fake_data.word(),
        "size": random.choice(["SMALL", "MEDIUM", "LARGE"]),
        "fragile": random.choice([True, False]),
        "offer": fake_data.random_int(100,1000)
    }
    token="abcdefg"

    mock_token.return_value = {"user_id": fake_data.random_int(1,100)}, 200
    response = app.test_client().post('/app_performance', json=data, headers={"Authorization": f'Bearer {token}'})
    response_info= json.loads(response.data.decode('utf-8'))
    assert response.status_code == 201
    offer_id = response_info['id']

    response = app.test_client().get('/app_performance/' + str(offer_id), headers={"Authorization": f'Bearer {token}'})
    response_info= json.loads(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert offer_id == response_info['id']

'''----------- Test get offer ivalid id --------------------'''
@patch('payments.views.get_token')
def test_get_offer_400(mock_token):
    token="abcdefg"
    mock_token.return_value = {"user_id": 1}, 200
    response = app.test_client().get('/app_performance/a', headers={"Authorization": f'Bearer {token}'})
    assert response.status_code == 400

'''----------- Test get offer not found --------------------'''
@patch('payments.views.get_token')
def test_get_offer_404(mock_token):
    token="abcdefg"
    mock_token.return_value = {"user_id": 1}, 200
    response = app.test_client().get('/app_performance/9999999', headers={"Authorization": f'Bearer {token}'})
    assert response.status_code == 404
