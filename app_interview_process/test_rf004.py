from app import app
import json
from faker import Faker
import unittest
from unittest.mock import patch
from faker.generator import random
from interview_process.handlers import endpoint_posts
from interview_process.handlers import endpoint_offers

fake_data = Faker()

'''----------- Test create offer success --------------------'''

@patch('interview_process.core.endpoint_posts')
@patch('interview_process.core.endpoint_users')
@patch('interview_process.core.endpoint_offers')

def test_crear_oferta(mock_endpoint_offers,
                               mock_endpoint_users,
                               mock_endpoint_posts,):
    data_create = {
            "description": "de user 2",
            "fragile": True,
            "offer": "5000",
            "size": "MEDIUM",
        }
    data_returned = {
            "createdAt": "2023-02-22",
            "description": "de user 2",
            "fragile": True,
            "id": 1,
            "offer": "5000",
            "postId": 1,
            "size": "MEDIUM",
            "userId": 1
        }
    token = "abcdefg"

    mock_endpoint_posts.return_value = (200,
                                        {
                                            "createdAt": "2023-02-23T19:29:31.709490",
                                            "id": 1,
                                            "plannedEndDate": "2023-03-11T00:00:00",
                                            "plannedStartDate": "2023-03-10T00:00:00",
                                            "routeId": 1,
                                            "userId": 2
                                        })

    mock_endpoint_users.return_value = (200,
                                        {
                                            "email": "a@b.com",
                                            "id": 1,
                                            "username": "a"
                                        }
                                        )

    
    mock_endpoint_offers.return_value = (201,
                                         data_returned)

    response = app.test_client().post('/app_interview_process/posts/1/app_performance', json=data_create, headers={"Authorization": f'Bearer {token}'})
    response_info = json.loads(response.data.decode('utf-8'))
    print(response_info)
    assert response.status_code == 201
    assert response_info['data']['id'] == 1


'''----------- Test create offer same user --------------------'''
@patch('interview_process.core.endpoint_posts')
@patch('interview_process.core.endpoint_users')
@patch('interview_process.core.endpoint_offers')
def test_crear_oferta_mismo_usuario(mock_endpoint_offers,
                               mock_endpoint_users,
                               mock_endpoint_posts,):
    data_create = {
            "description": "de user 2",
            "fragile": True,
            "offer": "5000",
            "size": "MEDIUM",
        }
    data_returned = {
            "createdAt": "2023-02-22",
            "description": "de user 2",
            "fragile": True,
            "id": 1,
            "offer": "5000",
            "postId": 1,
            "size": "MEDIUM",
            "userId": 1
        }
    token = "abcdefg"

    mock_endpoint_posts.return_value = (200,
                                        {
                                            "createdAt": "2023-02-23T19:29:31.709490",
                                            "id": 1,
                                            "plannedEndDate": "2023-03-11T00:00:00",
                                            "plannedStartDate": "2023-03-10T00:00:00",
                                            "routeId": 1,
                                            "userId": 1
                                        })

    mock_endpoint_users.return_value = (200,
                                        {
                                            "email": "a@b.com",
                                            "id": 1,
                                            "username": "a"
                                        }
                                        )

    
    mock_endpoint_offers.return_value = (201,
                                         data_returned)

    response = app.test_client().post('/app_interview_process/posts/1/app_performance', json=data_create, headers={"Authorization": f'Bearer {token}'})
    response_info = json.loads(response.data.decode('utf-8'))
    print(response_info)
    assert response.status_code == 412


'''----------- Test create offer wrong token --------------------'''
@patch('interview_process.core.endpoint_posts')
@patch('interview_process.core.endpoint_offers')
def test_crear_oferta_mal_token(mock_endpoint_offers,
                               mock_endpoint_posts,):
    data_create = {
            "description": "de user 2",
            "fragile": True,
            "offer": "5000",
            "size": "MEDIUM",
        }
    data_returned = {
            "createdAt": "2023-02-22",
            "description": "de user 2",
            "fragile": True,
            "id": 1,
            "offer": "5000",
            "postId": 1,
            "size": "MEDIUM",
            "userId": 1
        }
    token = {}

    mock_endpoint_posts.return_value = (200,
                                        {
                                            "createdAt": "2023-02-23T19:29:31.709490",
                                            "id": 1,
                                            "plannedEndDate": "2023-03-11T00:00:00",
                                            "plannedStartDate": "2023-03-10T00:00:00",
                                            "routeId": 1,
                                            "userId": 1
                                        })
    
    mock_endpoint_offers.return_value = (201,
                                         data_returned)

    response = app.test_client().post('/app_interview_process/posts/1/app_performance', json=data_create, headers=token)
    assert response.status_code == 401

'''----------- Test create offer success --------------------'''

@patch('interview_process.core.endpoint_posts')
@patch('interview_process.core.endpoint_users')
@patch('interview_process.core.endpoint_offers')

def test_crear_oferta_post_no_existe(mock_endpoint_offers,
                               mock_endpoint_users,
                               mock_endpoint_posts,):
    data_create = {
            "description": "de user 2",
            "fragile": True,
            "offer": "5000",
            "size": "MEDIUM",
        }
    data_returned = {
            "createdAt": "2023-02-22",
            "description": "de user 2",
            "fragile": True,
            "id": 1,
            "offer": "5000",
            "postId": 1,
            "size": "MEDIUM",
            "userId": 1
        }
    token = "abcdefg"

    mock_endpoint_posts.return_value = (404, "La publicacion no existe")

    mock_endpoint_users.return_value = (200,
                                        {
                                            "email": "a@b.com",
                                            "id": 1,
                                            "username": "a"
                                        }
                                        )
    
    mock_endpoint_offers.return_value = (201,
                                         data_returned)

    response = app.test_client().post('/app_interview_process/posts/10/app_performance', json=data_create, headers={"Authorization": f'Bearer {token}'})
    assert response.status_code == 404

def test_wrong_token_post():
    response =endpoint_posts("")
    assert response[0] == 401

def test_wrong_token_offer():
    response =endpoint_offers("")
    assert response[0] == 401
       