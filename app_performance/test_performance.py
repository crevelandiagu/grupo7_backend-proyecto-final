from app import app
import json
from faker import Faker
from unittest.mock import patch
from faker.generator import random

fake_data = Faker()


'''----------- Test ping --------------------'''
def test_ping():
    response = app.test_client().get('/performance/ping')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'pong'


'''----------- Test create performance success --------------------'''


def test_create_offer_200():
    data = {
        "candidateId": fake_data.random_int(1, 10),
        "companyId": fake_data.random_int(1, 10),
        "projectId": fake_data.random_int(1, 10),
        "employeeId": fake_data.random_int(1, 10),
        "score": fake_data.random_int(1, 10)
        }

    response = app.test_client().post('/performance/make-evaluation', json=data)
    response_info = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert response_info['message'] == 'Performance successfully added'


def test_create_offer_400():
    data = {
        "candidateId": fake_data.random_int(1, 10),
        "companyId": fake_data.random_int(1, 10),
        "projectId": fake_data.random_int(1, 10),
    }

    response = app.test_client().post('/performance/make-evaluation', json=data)
    response_info = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 422
    assert response_info[0].get('msg') == 'field required'


'''----------- Test get performance candidate --------------------'''


def test_get_performance_offer_200():
    data = {
        "candidateId": fake_data.random_int(1, 10),
        "companyId": fake_data.random_int(1, 10),
        "projectId": fake_data.random_int(1, 10),
        "employeeId": fake_data.random_int(1, 10),
        "score": fake_data.random_int(1, 10)
        }

    app.test_client().post('/performance/make-evaluation', json=data)

    response = app.test_client().get(f'/performance/candidate/{data.get("candidateId")}/evaluation')
    response_info = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert len(response_info) >= 1


def test_get_performance_offer_400():
    data = {
        "candidateId": '000000-0000000',
        }

    response = app.test_client().get(f'/performance/candidate/{data.get("candidateId")}/evaluation')

    assert response.status_code == 404