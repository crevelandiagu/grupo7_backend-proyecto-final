from app import app
from datetime import datetime, timedelta
from faker import Faker
from unittest.mock import patch

import json

fake_data = Faker()

def test_ping():
    response = app.test_client().get('/contracts/ping')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'pong'

def test_meke_contract_201_412():
    data = {
        "candidateId": fake_data.random_int(),
        "projectId": fake_data.random_int(),
        "companyId": fake_data.random_int(),
        "candidate_name": fake_data.name(),
        "project_name": fake_data.color_name(),
        "company_name": fake_data.company(),
    }

    response_data_201= app.test_client().post('/contracts/company/contract-made', json=data)

    response_data_contract_200 = app.test_client().get(f'/contracts/candidate/{data["candidateId"]}', json=data)
    response_data_contract_candidate_200 = app.test_client().get(f'/contracts/company/{data["companyId"]}', json=data)

    assert response_data_201.status_code == 200

    assert response_data_contract_200.status_code == 200
    assert response_data_contract_candidate_200.status_code == 200
