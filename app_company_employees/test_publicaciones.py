from app import app
from datetime import datetime, timedelta
from faker import Faker
from unittest.mock import patch

import json

fake = Faker()

def test_ping():
    response = app.test_client().get('/posts/ping')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'pong'

#==== create_post 200
@patch('company_employees.views.get_token')
def test_create_post_201(mock_token):
  #date_base = fake.date_time_this_decade(after_now=True, before_now=False).strftime('%Y-%m-%d')
  data = 	{
      "routeId": fake.random_int(1,1000),
      #"userId": fake.simple_profile()["username"],
      "plannedStartDate": (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d'),
      "plannedEndDate": (datetime.today() + timedelta(days=2)).strftime('%Y-%m-%d')
  }
  token=fake.pystr(min_chars=16, max_chars=16)

  mock_token.return_value = {"user_id": fake.random_int(1,10)}, 200
  response = app.test_client().post('/posts', json=data, headers={"Authorization": f'Bearer {token}'})
  response_info= json.loads(response.data.decode('utf-8'))
  assert response.status_code == 201
  assert response_info['id'] is not None
  assert len(list(response_info.keys())) == 3

@patch('company_employees.views.get_token')
def test_create_post_400(mock_token):
  data = 	{
    #"userId": fake.simple_profile()["username"],
    "plannedStartDate": (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d'),
    "plannedEndDate": (datetime.today() + timedelta(days=2)).strftime('%Y-%m-%d')
  }
  token=fake.pystr(min_chars=16, max_chars=16)

  mock_token.return_value = {"user_id": fake.random_int(1,10)}, 200
  response = app.test_client().post('/posts', json=data, headers={"Authorization": f'Bearer {token}'})
  assert response.status_code == 400

def test_create_post_401():
  data = 	{
    "routeId": fake.random_int(1,1000),
    #"userId": fake.simple_profile()["username"],
    "plannedStartDate": (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d'),
    "plannedEndDate": (datetime.today() + timedelta(days=2)).strftime('%Y-%m-%d')
  }
  response = app.test_client().post('/posts', json=data, headers={"Authorization": f'Bearer'})
  print(response)
  assert response.status_code == 401

@patch('company_employees.views.get_token')
def test_create_post_412a(mock_token):
  data = 	{
    "routeId": fake.random_int(1,1000),
    #"userId": fake.simple_profile()["username"],
    "plannedStartDate": datetime.today().strftime('%Y-%m-%d'),
    "plannedEndDate": datetime.today().strftime('%Y-%m-%d')
  }
  token=fake.pystr(min_chars=16, max_chars=16)

  mock_token.return_value = {"user_id": fake.random_int(1,10)}, 200
  response = app.test_client().post('/posts', json=data, headers={"Authorization": f'Bearer {token}'})
  assert response.status_code == 412

@patch('company_employees.views.get_token')
def test_create_post_412b(mock_token):
  data = 	{
    "routeId": fake.random_int(1,1000),
    #"userId": fake.simple_profile()["username"],
    "plannedStartDate": (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d'),
    "plannedEndDate": datetime.today().strftime('%Y-%m-%d')
  }
  token=fake.pystr(min_chars=16, max_chars=16)

  mock_token.return_value = {"user_id": fake.random_int(1,10)}, 200
  response = app.test_client().post('/posts', json=data, headers={"Authorization": f'Bearer {token}'})
  assert response.status_code == 412

#==== search_post
@patch('company_employees.views.get_token')
def test_search_post_when_200(mock_token):
  start_date = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')

  token=fake.pystr(min_chars=16, max_chars=16)

  mock_token.return_value = {"user_id": fake.random_int(1,10)}, 200
  response = app.test_client().get(f"/posts?when={start_date}", headers={"Authorization": f'Bearer {token}'})
  response_info= json.loads(response.data.decode('utf-8'))
  print(f"response_info {response_info}")
  assert response.status_code == 200

@patch('company_employees.views.get_token')
def test_search_post_route_200(mock_token):
  route = fake.random_int(1,1000)

  token=fake.pystr(min_chars=16, max_chars=16)

  mock_token.return_value = {"user_id": fake.random_int(1,10)}, 200
  response = app.test_client().get(f"/posts?route={route}", headers={"Authorization": f'Bearer {token}'})
  response_info= json.loads(response.data.decode('utf-8'))
  print(f"response_info {response_info}")
  assert response.status_code == 200

@patch('company_employees.views.get_token')
def test_search_post_filter_200(mock_token):
  filter = "me"
  token=fake.pystr(min_chars=16, max_chars=16)

  mock_token.return_value = {"user_id": fake.random_int(1,10)}, 200
  response = app.test_client().get(f"/posts?filter={filter}", headers={"Authorization": f'Bearer {token}'})
  response_info= json.loads(response.data.decode('utf-8'))
  print(f"response_info {response_info}")
  assert response.status_code == 200

@patch('company_employees.views.get_token')
def test_search_post__when_route_200(mock_token):
  start_date = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')
  route = fake.random_int(1,1000)
  token=fake.pystr(min_chars=16, max_chars=16)
  print(f"pruebas de ingreso")
  mock_token.return_value = {"user_id": fake.random_int(1,10)}, 200
  response = app.test_client().get(f"/posts?when={start_date}&route={route}", headers={"Authorization": f'Bearer {token}'})
  response_info= json.loads(response.data.decode('utf-8'))
  print(f"response_info {response_info}")
  assert response.status_code == 200

@patch('company_employees.views.get_token')
def test_search_post_when_filter_200(mock_token):
  start_date = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')
  filter = "me"
  token=fake.pystr(min_chars=16, max_chars=16)
  print(f"pruebas de ingreso")
  mock_token.return_value = {"user_id": fake.random_int(1,10)}, 200
  response = app.test_client().get(f"/posts?when={start_date}&filter={filter}", headers={"Authorization": f'Bearer {token}'})
  response_info= json.loads(response.data.decode('utf-8'))
  print(f"response_info {response_info}")
  assert response.status_code == 200

@patch('company_employees.views.get_token')
def test_search_post_route_filter_200(mock_token):
  route = fake.random_int(1,1000)
  filter = "me"
  token=fake.pystr(min_chars=16, max_chars=16)
  print(f"pruebas de ingreso")
  mock_token.return_value = {"user_id": fake.random_int(1,10)}, 200
  response = app.test_client().get(f"/posts?route={route}&filter={filter}", headers={"Authorization": f'Bearer {token}'})
  response_info= json.loads(response.data.decode('utf-8'))
  print(f"response_info {response_info}")
  assert response.status_code == 200

@patch('company_employees.views.get_token')
def test_search_post_all_200(mock_token):
  start_date = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d')
  route = fake.random_int(1,1000)
  filter = "me"
  token=fake.pystr(min_chars=16, max_chars=16)
  print(f"pruebas de ingreso")
  mock_token.return_value = {"user_id": fake.random_int(1,10)}, 200
  response = app.test_client().get(f"/posts?when={start_date}&route={route}&filter={filter}", headers={"Authorization": f'Bearer {token}'})
  response_info= json.loads(response.data.decode('utf-8'))
  print(f"response_info {response_info}")
  assert response.status_code == 200

@patch('company_employees.views.get_token')
def test_search_post_without_200(mock_token):
  token=fake.pystr(min_chars=16, max_chars=16)

  mock_token.return_value = {"user_id": fake.random_int(1,10)}, 200
  response = app.test_client().get(f"/posts", headers={"Authorization": f'Bearer {token}'})
  response_info= json.loads(response.data.decode('utf-8'))
  print(f"response_info {response_info}")
  assert response.status_code == 200

@patch('company_employees.views.get_token')
def test_search_when_400(mock_token):
  start_date = fake.word()
  token=fake.pystr(min_chars=16, max_chars=16)

  mock_token.return_value = {"user_id": fake.random_int(1,10)}, 200
  response = app.test_client().get(f"/posts?when={start_date}", headers={"Authorization": f'Bearer {token}'})
  response_info= json.loads(response.data.decode('utf-8'))
  print(f"response_info {response_info}")
  assert response.status_code == 400

@patch('company_employees.views.get_token')
def test_search_post_route_400(mock_token):
  route = fake.word()
  token=fake.pystr(min_chars=16, max_chars=16)

  mock_token.return_value = {"user_id": fake.random_int(1,10)}, 200
  response = app.test_client().get(f"/posts?route={route}", headers={"Authorization": f'Bearer {token}'})
  response_info= json.loads(response.data.decode('utf-8'))
  print(f"response_info {response_info}")
  assert response.status_code == 400

@patch('company_employees.views.get_token')
def test_search_post_filter_400(mock_token):
  filter = fake.word()
  token=fake.pystr(min_chars=16, max_chars=16)

  mock_token.return_value = {"user_id": fake.random_int(1,10)}, 200
  response = app.test_client().get(f"/posts?filter={filter}", headers={"Authorization": f'Bearer {token}'})
  response_info= json.loads(response.data.decode('utf-8'))
  print(f"response_info {response_info}")
  assert response.status_code == 400

def test_search_post_route_401():

  response = app.test_client().get('/posts', headers={"Authorization": f'Bearer'})
  print(response)
  assert response.status_code == 401

#==== get_post
@patch('company_employees.views.get_token')
def test_get_post_200(mock_token):
  id = 1
  token=fake.pystr(min_chars=16, max_chars=16)

  mock_token.return_value = {"user_id": fake.random_int(1,10)}, 200
  response = app.test_client().get(f"/posts/{id}", headers={"Authorization": f'Bearer {token}'})
  response_info= json.loads(response.data.decode('utf-8'))
  print(f"response_info {response_info}")
  assert response.status_code == 200
  assert len(list(response_info.keys())) == 6

@patch('company_employees.views.get_token')
def test_get_post_400(mock_token):
  id = fake.word()
  token=fake.pystr(min_chars=16, max_chars=16)

  mock_token.return_value = {"user_id": fake.random_int(1,10)}, 200
  response = app.test_client().get(f"/posts/{id}", headers={"Authorization": f'Bearer {token}'})
  assert response.status_code == 400

def test_get_post_401():
  response = app.test_client().get('/posts', headers={"Authorization": f'Bearer'})
  assert response.status_code == 401

@patch('company_employees.views.get_token')
def test_get_post_404(mock_token):
  id = 0
  token=fake.pystr(min_chars=16, max_chars=16)

  mock_token.return_value = {"user_id": fake.random_int(1,10)}, 200
  response = app.test_client().get(f"/posts/{id}", headers={"Authorization": f'Bearer {token}'})
  assert response.status_code == 404
  


