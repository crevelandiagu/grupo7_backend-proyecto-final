from app import app
import json
from faker import Faker

fake_data = Faker()
'''----------- Test ping --------------------'''


def test_ping():
    response = app.test_client().get('/candidate/ping')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'pong'


'''----------- Test sign in --------------------'''


def test_user_singup_201_412():
    data = {
        "password": "Abcdef1!",#fake_data.password(),
        "email": "alguien@algo.com"#fake_data.email()
    }

    response_data_201 = app.test_client().post('/candidate/signup', json=data)
    response_info_201 = json.loads(response_data_201.data.decode('utf-8'))

    response_data_412 = app.test_client().post('/candidate/signup', json=data)
    response_info_412 = json.loads(response_data_412.data.decode('utf-8'))

    assert response_data_201.status_code == 201
    #assert list(response_info_201.keys()) == ['createdAt', 'email', 'id', 'mensaje']

    assert response_data_412.status_code == 412
    #assert response_info_412['mensaje'] == 'El usuario ya existe, pruebe con otro'

#
# def test_user_singin_400():
#     data = {
#         "username": fake_data.name(),
#         "password": fake_data.name()
#     }
#     response_data = app.test_client().post('/app_company', json=data)
#     response_info = json.loads(response_data.data.decode('utf-8'))
#
#     assert response_data.status_code == 400
#     assert response_info['mensaje'] == "falta 'email'"
#
#
'''----------- Test log in --------------------'''



def test_user_login_200_400():

    data = {
        "password": fake_data.password(),
        "email": fake_data.email()
    }

    app.test_client().post('/candidate/signup', json=data)

    data_login = {"email": data['email'],
                  "password": data['password'],
                  }

    response_data_200 = app.test_client().post('/candidate/login', json=data_login)
    response_info_200 = json.loads(response_data_200.data.decode('utf-8'))

    data_login_miss = {
        "email": data['email']
                  }

    response_data_400 = app.test_client().post('/candidate/login', json=data_login_miss)
    response_info_400 = json.loads(response_data_400.data.decode('utf-8'))

    assert response_data_200.status_code == 200
    assert len(list(response_info_200.keys())) == 3

    assert response_data_400.status_code == 400
    assert response_info_400['mensaje'] == "falta 'password'"


def test_user_singin_404():
    data = {
        "password": fake_data.password(),
        "email": fake_data.email()
    }
    response_data_404 = app.test_client().post('/candidate/login', json=data)
    response_info_404 = json.loads(response_data_404.data.decode('utf-8'))

    assert response_data_404.status_code == 404
    assert response_info_404['mensaje'] == "Usuario con username no exista o contrasena incorrecta"


# '''----------- Test me --------------------'''
#
#
# def test_user_me_200_401():
#
#     data = {"username": fake_data.name(),
#             "password": fake_data.name(),
#             "email": fake_data.name()}
#
#     app.test_client().post('/app_company', json=data)
#
#     data_login = {"username": data['username'],
#                   "password": data['password'],
#                   }
#
#     response_data = app.test_client().post('/app_company/auth', json=data_login)
#     response_info = json.loads(response_data.data.decode('utf-8'))
#
#     response_data_200 = app.test_client().get("/app_company/me", headers={"Authorization": "Basic {}".format(response_info['token'])})
#     response_info_200 = json.loads(response_data_200.data.decode('utf-8'))
#
#     assert response_data_200.status_code == 200
#     assert len(list(response_info_200.keys())) == 3
#
#
# def test_user_me_400():
#
#     response_data_400 = app.test_client().get("/app_company/me")
#     response_info_400 = json.loads(response_data_400.data.decode('utf-8'))
#
#     assert response_data_400.status_code == 400
#     assert response_info_400['mensaje'] == "No viene token"
#
#
# def test_user_me_401():
#
#     response_data_401 = app.test_client().get("/app_company/me", headers={"Authorization": "Basic token"})
#     response_info_401 = json.loads(response_data_401.data.decode('utf-8'))
#
#     assert response_data_401.status_code == 401
#     assert response_info_401['mensaje'] == "token no válido"
