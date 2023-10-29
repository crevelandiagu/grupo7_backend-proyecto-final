from app import app
import json
from faker import Faker

fake_data = Faker()
'''----------- Test ping --------------------'''


def test_ping():
    response = app.test_client().get('/interviews/ping')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'pong'


'''----------- Test create interview --------------------'''


def test_interviews_create_201_412():
    data = {
        "dateTime":fake_data.iso8601(),
        "candidateName":fake_data.name(),
        "interviewStatus":fake_data.word(),
        "candidateId": fake_data.random_int(),
        "companyId": fake_data.random_int(),
        "companyEmployeeId": fake_data.random_int(),
        "projectId": fake_data.random_int()
    }
    data1 = {
        "dateTime":"",
        "candidateName":fake_data.name(),
        "interviewStatus":fake_data.word(),
        "candidateId": fake_data.random_int(),
        "companyId": fake_data.random_int(),
        "companyEmployeeId": fake_data.random_int(),
        "projectId": fake_data.random_int()
    }

    data2 = {
        "dateTime":fake_data.iso8601(),
        "candidateName":fake_data.name(),
        "interviewStatus":fake_data.word(),
        "candidateId": fake_data.random_int(),
        "companyId": fake_data.word(),
        "companyEmployeeId": fake_data.random_int(),
        "projectId": fake_data.random_int()
    }


    response_data_201 = app.test_client().post('/interviews/', json=data)
    response_data_datetime_412 = app.test_client().post('/interviews/', json=data1)
    response_data_company_id_412 = app.test_client().post('/interviews/', json=data2)

    assert response_data_201.status_code == 201
    assert response_data_datetime_412.status_code == 412
    assert response_data_company_id_412.status_code == 412


'''----------- Test get interviews company --------------------'''


def test_get_interviews_company_200_404():

    data = {
        "dateTime":fake_data.iso8601(),
        "candidateName":fake_data.name(),
        "interviewStatus":fake_data.word(),
        "candidateId": fake_data.random_int(),
        "companyId": fake_data.random_int(),
        "companyEmployeeId": fake_data.random_int(),
        "projectId": fake_data.random_int()
    }

    response_create_201 = app.test_client().post('/interviews/', json=data)

    assert response_create_201.status_code == 201    

    response_data_200 = app.test_client().get(f'/interviews/company/{data.get("companyId")}')
    response_info_200 = json.loads(response_data_200.data.decode('utf-8'))
    
    assert response_data_200.status_code == 200
    assert len(response_info_200) == 1

    response_data_404 = app.test_client().get('/interviews/company/')
    assert response_data_404.status_code == 404



'''----------- Test get interviews candidate --------------------'''


def test_get_interviews_candidate_200_404():

    data = {
        "dateTime":fake_data.iso8601(),
        "candidateName":fake_data.name(),
        "interviewStatus":fake_data.word(),
        "candidateId": fake_data.random_int(),
        "companyId": fake_data.random_int(),
        "companyEmployeeId": fake_data.random_int(),
        "projectId": fake_data.random_int()
    }

    response_create_201 = app.test_client().post('/interviews/', json=data)

    assert response_create_201.status_code == 201    

    response_data_200 = app.test_client().get(f'/interviews/candidate/{data.get("candidateId")}')
    response_info_200 = json.loads(response_data_200.data.decode('utf-8'))
    
    assert response_data_200.status_code == 200
    assert len(response_info_200) == 1

    response_data_404 = app.test_client().get('/interviews/candidate/')
    assert response_data_404.status_code == 404


def test_interviews_score_201_412_404():
    
    data = {
        "dateTime":fake_data.iso8601(),
        "candidateName":fake_data.name(),
        "interviewStatus":fake_data.word(),
        "candidateId": fake_data.random_int(),
        "companyId": fake_data.random_int(),
        "companyEmployeeId": fake_data.random_int(),
        "projectId": fake_data.random_int()
    }


    response_data_201 = app.test_client().post('/interviews/', json=data)
    
    response_data_200 = app.test_client().get(f'/interviews/company/{data.get("companyId")}')
    response_info_200 = json.loads(response_data_200.data.decode('utf-8'))

    response_data_score_201 = app.test_client().post(f'/interviews/score/{response_info_200[0]["id"]}/', json={"score": fake_data.random_int()})

    response_data_404 = app.test_client().post(f'/interviews/score/{fake_data.random_int()}', json={"score": fake_data.random_int()})
    response_data_412 =  app.test_client().post(f'/interviews/score/{response_info_200[0]["id"]}/', json={"score": fake_data.word()})

    assert response_data_201.status_code == 201
    assert response_data_score_201.status_code == 201
    assert response_data_404.status_code == 404
    assert response_data_412.status_code == 412