from app import app
import json
from faker import Faker
from unittest.mock import patch
fake_data = Faker()

'''----------- Test ping --------------------'''


def test_ping():
    response = app.test_client().get('/projects/ping')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'pong'


'''----------- Test create project --------------------'''

# trayectos.views.get_token
# project.factory.get_company
@patch('project.core.get_company')
def test_projects_create_201_412(mock_token):
    data = {
        "projectName": fake_data.word(),
        "description": fake_data.text(max_nb_chars=100),
        "companyId": fake_data.random_int()
    }
    data1 = {
        "description": fake_data.text(max_nb_chars=100),
        "companyId": fake_data.random_int()
    }

    data2 = {
        "projectName": fake_data.word(),
        "description": fake_data.text(max_nb_chars=100)
    }
    data3 = {
        "projectName": fake_data.word(),
        "description": fake_data.text(max_nb_chars=400),
        "companyId": fake_data.random_int()
    }
    mock_token.return_value = dict()
    response_data_201 = app.test_client().post('/projects/', json=data)
    response_data_project_name_412 = app.test_client().post('/projects/', json=data1)
    response_data_company_id_412 = app.test_client().post('/projects/', json=data2)
    response_data_long_description_201 = app.test_client().post('/projects/', json=data3)

    assert response_data_201.status_code == 201
    assert response_data_project_name_412.status_code == 422
    assert response_data_company_id_412.status_code == 422
    assert response_data_long_description_201.status_code == 201


'''----------- Test get projects --------------------'''


def test_get_projects_200_400_404():

    data = {
        "projectName": fake_data.word(),
        "description": fake_data.text(max_nb_chars=100),
        "companyId": fake_data.random_int()
    }

    response_create_201 = app.test_client().post('/projects/', json=data)

    assert response_create_201.status_code == 201    

    response_data_200 = app.test_client().get(f'/projects?companyId={data.get("companyId")}')
    response_info_200 = json.loads(response_data_200.data.decode('utf-8'))
    
    assert response_data_200.status_code == 200
    assert len(response_info_200) == 1

    response_data_400 = app.test_client().get('/projects')
    assert response_data_400.status_code == 422

    response_data_404 = app.test_client().get(f'/projects?companyId={data.get("companyId")+1}')
    assert response_data_404.status_code == 200

def test_candidate_project():
    from project.candidate_project import add_candidate_project
    message_start_process = {
        "where": "candidate-chosen-one",
        "candidateId": 1,
        "projectId": 1,
        "companyId": 1,

    }
    data = add_candidate_project(message_start_process)