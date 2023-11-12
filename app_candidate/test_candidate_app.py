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
        "password": fake_data.password(),
        "email": f"{fake_data.first_name()}@gmail.com"
    }

    response_data_201 = app.test_client().post('/candidate/signup', json=data)
    response_info_201 = json.loads(response_data_201.data.decode('utf-8'))

    response_data_412 = app.test_client().post('/candidate/signup', json=data)
    response_info_412 = json.loads(response_data_412.data.decode('utf-8'))

    assert response_data_201.status_code == 200
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
        "email": f"{fake_data.first_name()}@gmail.com"
    }

    response_create_201 = app.test_client().post('/candidate/signup', json=data)

    assert response_create_201.status_code == 200

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
    # assert len(list(response_info_200.keys())) == 3

    assert response_data_400.status_code == 422
    # assert response_info_400['mensaje'] == "falta 'password'"


def test_user_singin_404():
    data = {
        "password": fake_data.password(),
        "email": fake_data.first_name()+'.'+fake_data.last_name()+"@"+fake_data.last_name()+".com"
    }
    response_data_404 = app.test_client().post('/candidate/login', json=data)
    response_info_404 = json.loads(response_data_404.data.decode('utf-8'))

    assert response_data_404.status_code == 404
    assert response_info_404['mensaje'] == "Usuario con username no exista o contrasena incorrecta"


'''----------- Test CV --------------------'''


def test_user_cv_basicinfo_get_post_200():

    data_signup = {
        "password": fake_data.password(),
        "email": f"{fake_data.first_name()}@gmail.com"
    }

    response = app.test_client().post('/candidate/signup', json=data_signup)
    response_info_200 = json.loads(response.data.decode('utf-8'))
    candidate_id = response_info_200.get('id', 1)

    data = {
        "name": fake_data.name(),
        "lastname": fake_data.last_name(),
        "birthdate": fake_data.date(),
        "nacionality": fake_data.city(),
        "phone_number": fake_data.phone_number(),
        "number_id": fake_data.phone_number()
    }

    response_basicinfo_post = app.test_client().post(f'/candidate/profile/basicinfo/{candidate_id}', json=data)
    response_basicinfo_get = app.test_client().get(f'/candidate/profile/basicinfo/{candidate_id}', json=data)


    assert response_basicinfo_post.status_code == 200
    assert response_basicinfo_get.json.get('name') == data.get('name')


def test_user_cv_experience_get_post_200():

    data_signup = {
        "password": fake_data.password(),
        "email": f"{fake_data.first_name()}@gmail.com"
    }

    response = app.test_client().post('/candidate/signup', json=data_signup)
    response_info_200 = json.loads(response.data.decode('utf-8'))
    candidate_id = response_info_200.get('id', 1)

    data = {
        "position": fake_data.name(),
        "company_name": fake_data.company(),
        "start_date": fake_data.date(),
        "end_date": fake_data.date(),
        "place": fake_data.city(),
        "skills": ["Python", "Java"]

    }

    response_basicinfo_post = app.test_client().post(f'/candidate/profile/experience/{candidate_id}', json=data)
    response_basicinfo_get = app.test_client().get(f'/candidate/profile/experience/{candidate_id}', json=data)


    assert response_basicinfo_post.status_code == 200
    assert response_basicinfo_get.json.get('experience')[0].get('position') == data.get('position')


def test_user_cv_education_get_post_200():

    data_signup = {
        "password": fake_data.password(),
        "email": f"{fake_data.first_name()}@gmail.com"
    }

    response = app.test_client().post('/candidate/signup', json=data_signup)
    response_info_200 = json.loads(response.data.decode('utf-8'))
    candidate_id = response_info_200.get('id', 1)

    data = {
        "university": fake_data.company(),
        "subject":  fake_data.name(),
        "start_date": fake_data.date(),
        "end_date": fake_data.date(),
        "skills": ["Python", "Java"]
    }

    response_basicinfo_post = app.test_client().post(f'/candidate/profile/education/{candidate_id}', json=data)
    response_basicinfo_get = app.test_client().get(f'/candidate/profile/education/{candidate_id}', json=data)


    assert response_basicinfo_post.status_code == 200
    assert response_basicinfo_get.json.get('education')[0].get('university') == data.get('university')


def test_user_cv_certificates_get_post_200():

    data_signup = {
        "password": fake_data.password(),
        "email": f"{fake_data.first_name()}@gmail.com"
    }

    response = app.test_client().post('/candidate/signup', json=data_signup)
    response_info_200 = json.loads(response.data.decode('utf-8'))
    candidate_id = response_info_200.get('id', 1)

    data = {

        "name_certificate": fake_data.company(),
        "company": fake_data.company(),
        "expedition_date": fake_data.date(),
        "date_expiry": fake_data.date(),

    }

    response_basicinfo_post = app.test_client().post(f'/candidate/profile/certificates/{candidate_id}', json=data)
    response_basicinfo_get = app.test_client().get(f'/candidate/profile/certificates/{candidate_id}', json=data)


    assert response_basicinfo_post.status_code == 200
    assert response_basicinfo_get.json.get('certificates')[0].get('name_certificate') == data.get('name_certificate')

