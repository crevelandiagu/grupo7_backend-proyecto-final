# from app import app
# from datetime import datetime, timedelta
# from faker import Faker
# from unittest.mock import patch
#
# fake = Faker()
#
# def test_ping():
#     response = app.test_client().get('/app_selection_process/ping')
#     assert response.status_code == 200
#     assert response.data.decode('utf-8') == 'pong'
#
# #==== creacion_publicacion 201
# @patch('interview_process.core.endpoint_journey')
# @patch('interview_process.core.endpoint_posts')
# def test_creacion_publicacion_201(mock_posts, mock_journey):
#    data = {
#       "plannedStartDate": (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d'),
#       "plannedEndDate": (datetime.today() + timedelta(days=2)).strftime('%Y-%m-%d'),
#       "origin": {
#          "airportCode": fake.currency_code(),
#          "country": fake.currency_code()
#       },
#       "destiny": {
#          "airportCode": fake.currency_code(),
#          "country": fake.currency_code()
#       },
#       "bagCost": fake.random_int(100,10000)
#    }
#
#    create_journey_data = {
#        "createAt": (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d'),
#        "expireAt": (datetime.today() + timedelta(days=30)).strftime('%Y-%m-%d'),
#        "id": fake.random_int(1,100)
#    }
#
#    create_posts_data = {
#       "createdAt": (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d'),
#       "id": fake.random_int(1,100),
#       "userId": fake.random_int(1,100)
#    }
#
#    mock_journey.side_effect = [(200, []), (201, [create_journey_data])]
#    mock_posts.side_effect = [(201, create_posts_data)]
#
#    token=fake.pystr(min_chars=16, max_chars=16)
#    header = {
#        "Authorization": f'Bearer {token}'
#    }
#
#    response = app.test_client().post('/app_selection_process/posts', json=data, headers=header)
#    assert response.status_code == 201
#
# #==== creacion_publicacion 400
# def test_creacion_publicacion_400():
#    data = {
#       "plannedStartDate": (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d'),
#       "plannedEndDate": (datetime.today() + timedelta(days=2)).strftime('%Y-%m-%d'),
#       "origin": {
#          "airportCode": fake.currency_code(),
#          "country": fake.currency_code()
#       },
#       "destiny": {
#          "airportCode": fake.currency_code(),
#          "country": fake.currency_code()
#       }
#    }
#
#    token=fake.pystr(min_chars=16, max_chars=16)
#    header = {
#        "Authorization": f'Bearer {token}'
#    }
#
#    response = app.test_client().post('/app_selection_process/posts', json=data, headers=header)
#    assert response.status_code == 400
#
# #==== creacion_publicacion 401
# def test_creacion_publicacion_401():
#    header = {}
#
#    data = {
#       "plannedStartDate": (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d'),
#       "plannedEndDate": (datetime.today() + timedelta(days=2)).strftime('%Y-%m-%d'),
#       "origin": {
#          "airportCode": fake.currency_code(),
#          "country": fake.currency_code()
#       },
#       "destiny": {
#          "airportCode": fake.currency_code(),
#          "country": fake.currency_code()
#       },
#       "bagCost": fake.random_int(100,10000)
#    }
#
#    response = app.test_client().post('/app_selection_process/posts', json=data, headers=header)
#    assert response.status_code == 401
#
# #==== creacion_publicacion 412
# @patch('interview_process.core.endpoint_journey')
# @patch('interview_process.core.endpoint_posts')
# def test_creacion_publicacion_201(mock_posts, mock_journey):
#    data = {
#       "plannedStartDate": (datetime.today() + timedelta(days=60)).strftime('%Y-%m-%d'),
#       "plannedEndDate": (datetime.today() + timedelta(days=61)).strftime('%Y-%m-%d'),
#       "origin": {
#          "airportCode": fake.currency_code(),
#          "country": fake.currency_code()
#       },
#       "destiny": {
#          "airportCode": fake.currency_code(),
#          "country": fake.currency_code()
#       },
#       "bagCost": fake.random_int(100,10000)
#    }
#
#    create_journey_data = {
#        "createAt": (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d'),
#        "expireAt": (datetime.today() + timedelta(days=30)).strftime('%Y-%m-%d'),
#        "id": fake.random_int(1,100)
#    }
#
#    err_create_posts_data = {
#       "mensaje": "Fecha final debe ser mayor a fecha inicial",
#    }
#
#    mock_journey.side_effect = [(200, []), (201, [create_journey_data]), (204, {"mesage":"Deleted"})]
#    mock_posts.side_effect = [(412, err_create_posts_data)]
#
#    token=fake.pystr(min_chars=16, max_chars=16)
#    header = {
#        "Authorization": f'Bearer {token}'
#    }
#
#    response = app.test_client().post('/app_selection_process/posts', json=data, headers=header)
#    assert response.status_code == 412
#
#
#
#
#
#
