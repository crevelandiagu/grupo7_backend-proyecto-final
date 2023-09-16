from app import app
import json
from faker import Faker
import unittest
from unittest.mock import patch
from faker.generator import random

fake_data = Faker()

'''----------- Test create offer success --------------------'''

@patch('interview_process.core.endpoint_posts')
@patch('interview_process.core.endpoint_users')
@patch('interview_process.core.endpoint_journey')
@patch('interview_process.core.endpoint_offers')
def test_consultar_publicacion(mock_endpoint_offers,
                               mock_endpoint_journey,
                               mock_endpoint_users,
                               mock_endpoint_posts,):
    data = {}
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
                                            "id": 2,
                                            "username": "a"
                                        }
                                        )

    mock_endpoint_journey.return_value = (200,
                                          [
                                              {
                                                  "bagCost": "205.00",
                                                  "destinyAirportCode": "JHI",
                                                  "destinyCountry": "us",
                                                  "id": 1,
                                                  "sourceAirportCode": "HGY",
                                                  "sourceCountry": "decade"
                                              }
                                          ]
                                          )
    mock_endpoint_offers.return_value = (200,
                                         DATA_OFFERS)

    response = app.test_client().get('/app_interview_process/posts/1', json=data, headers={"Authorization": f'Bearer {token}'})
    response_info = json.loads(response.data.decode('utf-8'))
    print(response_info)
    assert response.status_code == 200
    assert response_info['data']['createdAt'] == "2023-02-23T19:29:31.709490"
    assert len(response_info['data']['app_performance']) > 1

global DATA_OFFERS
DATA_OFFERS = [
        {
            "createdAt": "2023-02-22",
            "description": "de user 2",
            "fragile": True,
            "id": 1,
            "offer": "5000",
            "postId": 100,
            "size": "MEDIUM",
            "userId": 1
        },
        {
            "createdAt": "2023-02-22",
            "description": "de user 2",
            "fragile": True,
            "id": 2,
            "offer": "5000",
            "postId": 100,
            "size": "MEDIUM",
            "userId": 1
        },
        {
            "createdAt": "2023-02-22",
            "description": "de user 2",
            "fragile": True,
            "id": 3,
            "offer": "5000",
            "postId": 100,
            "size": "MEDIUM",
            "userId": 1
        },
        {
            "createdAt": "2023-02-22",
            "description": "de user 2",
            "fragile": True,
            "id": 4,
            "offer": "5000",
            "postId": 100,
            "size": "MEDIUM",
            "userId": 1
        },
        {
            "createdAt": "2023-02-22",
            "description": "de user 2",
            "fragile": True,
            "id": 5,
            "offer": "5000",
            "postId": 100,
            "size": "MEDIUM",
            "userId": 1
        },
        {
            "createdAt": "2023-02-22",
            "description": "de user 2",
            "fragile": True,
            "id": 6,
            "offer": "5000",
            "postId": 100,
            "size": "MEDIUM",
            "userId": 1
        },
        {
            "createdAt": "2023-02-22",
            "description": "de user 2",
            "fragile": True,
            "id": 7,
            "offer": "5000",
            "postId": 100,
            "size": "MEDIUM",
            "userId": 1
        },
        {
            "createdAt": "2023-02-23",
            "description": "de user 2",
            "fragile": True,
            "id": 8,
            "offer": "5000",
            "postId": 100,
            "size": "MEDIUM",
            "userId": 2
        },
        {
            "createdAt": "2023-02-23",
            "description": "de user 2",
            "fragile": True,
            "id": 9,
            "offer": "5000",
            "postId": 1,
            "size": "MEDIUM",
            "userId": 2
        },
        {
            "createdAt": "2023-02-23",
            "description": "de user 2",
            "fragile": True,
            "id": 10,
            "offer": "4000",
            "postId": 1,
            "size": "MEDIUM",
            "userId": 2
        },
        {
            "createdAt": "2023-02-23",
            "description": "de user 2",
            "fragile": True,
            "id": 11,
            "offer": "3000",
            "postId": 1,
            "size": "MEDIUM",
            "userId": 2
        },
        {
            "createdAt": "2023-02-23",
            "description": "de user 2",
            "fragile": True,
            "id": 12,
            "offer": "2000",
            "postId": 1,
            "size": "MEDIUM",
            "userId": 2
        },
        {
            "createdAt": "2023-02-23",
            "description": "de user 2",
            "fragile": True,
            "id": 13,
            "offer": "1000",
            "postId": 1,
            "size": "MEDIUM",
            "userId": 2
        }
    ]
