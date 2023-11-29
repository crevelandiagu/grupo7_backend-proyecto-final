from app import app
import json
from faker import Faker

fake_data = Faker()
'''----------- Test ping --------------------'''


def test_ping():
    response = app.test_client().get('/company/ping')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'pong'


'''----------- Test sign in --------------------'''
#
#
def test_user_singin_201_412():
    data = {
        "password": fake_data.password(),
        "email": fake_data.email(),
        "name": fake_data.name()
    }

    response_data_201 = app.test_client().post('/company/signup', json=data)
    response_info_201 = json.loads(response_data_201.data.decode('utf-8'))

    response_data_412 = app.test_client().post('/company/signup', json=data)
    response_info_412 = json.loads(response_data_412.data.decode('utf-8'))

    assert response_data_201.status_code == 200
    # assert list(response_info_201.keys()) == ['createdAt', 'id']

    assert response_data_412.status_code == 412
    # assert response_info_412['mensaje'] == 'El usuario ya existe, pruebe con otro'


def test_user_basicinfo_201_412():
    data = {
        "password": fake_data.password(),
        "email": fake_data.email(),
        "name": fake_data.name()
    }

    response_data_201 = app.test_client().post('/company/signup', json=data)
    response_info_201 = json.loads(response_data_201.data.decode('utf-8'))

    response_data_412 = app.test_client().get('/company/profile/basicinfo/1', json=data)
    response_info_412 = json.loads(response_data_412.data.decode('utf-8'))

    assert response_data_201.status_code == 200
    # assert list(response_info_201.keys()) == ['createdAt', 'id']

    assert response_data_412.status_code == 200
    # assert response_info_412['mensaje'] == 'El usuario ya existe, pruebe con otro'