from app import app
from datetime import datetime, timedelta
from faker import Faker
from unittest.mock import patch

import json

fake = Faker()

'----------------------------test ping -----------------------------------------------'
def test_ping():
    response = app.test_client().get('/search-tool/ping')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'pong'

'---------------------------------test search skill ------------------------------------------'
@patch('search_tool.core.run_query')
def test_search_skills_400(run_query):
    "search-tool/search?skill=Python-Java"


    run_query.return_value = {'message': 'error'}
    response = app.test_client().get('/search-tool/search?skill=Python-Java')
    response_info = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 400
    assert run_query.return_value == response_info

@patch('search_tool.core.run_query')
def test_search_skills_200(run_query):
    "search-tool/search?skill=Python-Java"

    data = [(
        fake.random_number(),
        {'skills': ['Python', 'Java', "Go"]},
        fake.random_number(),
        fake.name(),
        fake.last_name(),
        2,
    )]

    run_query.return_value = data
    response = app.test_client().get('/search-tool/search?skill=Python-Java')
    response_info = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert len(response_info) == 1

'-------------------------------------test search years exp --------------------------------------'


@patch('search_tool.core.run_query')
def test_search_year_exp_400(run_query):

    run_query.return_value = {'message': 'error'}
    response = app.test_client().get('/search-tool/search?experienceYears=3')
    response_info = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 400
    assert run_query.return_value == response_info

@patch('search_tool.core.run_query')
def test_search_year_exp_200(run_query):

    data = [(
        fake.random_number(),
        {'skills': ['Python', 'Java', "Go"]},
        fake.random_number(),
        fake.name(),
        fake.last_name(),
        2,
    )]

    run_query.return_value = data
    response = app.test_client().get('/search-tool/search?experienceYears=3')
    response_info = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert len(response_info) == 1

@patch('search_tool.core.run_query')
def test_search_year_exp_empty_200(run_query):

    data = []

    run_query.return_value = data
    response = app.test_client().get('/search-tool/search?experienceYears=3')
    response_info = json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200
    assert len(response_info) == 0