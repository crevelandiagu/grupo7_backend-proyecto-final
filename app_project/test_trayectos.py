from app import app
import json
from faker import Faker
from unittest.mock import patch
from faker.generator import random
import datetime

fake_data = Faker()

'''----------- Test ping --------------------'''
def test_ping():
    response = app.test_client().get('/routes/ping')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'pong'


'''----------- Test crear trayecto --------------------'''
@patch('project.views.get_token')
def test_crear_trayecto_201(mock_token):
    data = 	{
        "sourceAirportCode": fake_data.word(ext_word_list=["ABF", "JHI", "LKO", "IJH", "HGY", "LLO", "WOD","PLS"]),
        "destinyAirportCode": fake_data.word(ext_word_list=["ABF", "JHI", "LKO", "IJH", "HGY", "LLO", "WOD","PLS"]),
        "destinyCountry": fake_data.word(),
        "bagCost": fake_data.random_int(10,600),
        "sourceCountry": fake_data.word()
    }

    token="abcdefg"
    
    mock_token.return_value = {"user_id": fake_data.random_int(1,10)}, 200
    response = app.test_client().post('/routes', json=data, headers={"Authorization": f'Bearer {token}'})    
    response_info= json.loads(response.data.decode('utf-8'))
    assert response.status_code == 201
   # assert response_info[0]['id']== data['id']
   #  assert len(list(response_info.keys())) == 3



@patch('project.views.get_token')
def test_crear_trayecto_401(mock_token):

    data = 	{
        "sourceAirportCode": fake_data.word(ext_word_list=["ABF", "JHI", "LKO", "IJH", "HGY", "LLO", "WOD","PLS"]),
        "destinyAirportCode": fake_data.word(ext_word_list=["ABF", "JHI", "LKO", "IJH", "HGY", "LLO", "WOD","PLS"]),
        "destinyCountry": fake_data.word(),
        "bagCost": fake_data.random_int(10,600),
        "sourceCountry": fake_data.word()
    }

    token = "iisjsu"

    mock_token.return_value = "Invalid token", 401
    response = app.test_client().post("/routes", json=data)
    assert response.status_code == 401

@patch('project.views.get_token')
def test_obtener_todos_los_trayectos(mock_token):

    data = 	{
        "sourceAirportCode": fake_data.word(ext_word_list=["ABF", "JHI", "LKO", "IJH", "HGY", "LLO", "WOD","PLS"]),
        "destinyAirportCode": fake_data.word(ext_word_list=["ABF", "JHI", "LKO", "IJH", "HGY", "LLO", "WOD","PLS"]),
        "destinyCountry": fake_data.word(),
        "bagCost": fake_data.random_int(10,600),
        "sourceCountry": fake_data.word()
    }

    token = "iisjsu"
    
    # crear trayecto
    mock_token.return_value = {"user_id": fake_data.random_int(1,10)}, 200
    response = app.test_client().post("/routes", json=data, headers={"Authorization": f'Bearer {token}'})
    response_info= json.loads(response.data.decode('utf-8'))
    assert response.status_code == 201
 

    # obtener project
    response = app.test_client().get("/routes", json=data, headers={"Authorization": f'Bearer {token}'})
    response_info= json.loads(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert len(response_info) == 2


@patch('project.views.get_token')
def test_crear_trayecto_bagCost_igual_a_cero_400(mock_token):

    data = 	{
        "sourceAirportCode": fake_data.word(ext_word_list=["ABF", "JHI", "LKO", "IJH", "HGY", "LLO", "WOD","PLS"]),
        "destinyAirportCode": fake_data.word(ext_word_list=["ABF", "JHI", "LKO", "IJH", "HGY", "LLO", "WOD","PLS"]),
        "destinyCountry": fake_data.word(),
        "bagCost": 0,
        "sourceCountry": fake_data.word()
    }

    token = "iisjsu"
    
    # crear trayecto
    mock_token.return_value = {"user_id": fake_data.random_int(1,10)}, 200
    response = app.test_client().post("/routes", json=data, headers={"Authorization": f'Bearer {token}'})
    response_info= json.loads(response.data.decode('utf-8'))
    assert response.status_code == 400


 
@patch('project.views.get_token')
def test_crear_trayecto_bagCost_igual_a_cero_400(mock_token):

    data = 	{
        "sourceAirportCode": fake_data.word(ext_word_list=["ABF", "JHI", "LKO", "IJH", "HGY", "LLO", "WOD","PLS"]),
        "destinyAirportCode": fake_data.word(ext_word_list=["ABF", "JHI", "LKO", "IJH", "HGY", "LLO", "WOD","PLS"]),
        "destinyCountry": fake_data.word(),
        "bagCost": 0,
        "sourceCountry": fake_data.word()
    }

    token = "iisjsu"
    
    # crear trayecto
    mock_token.return_value = {"user_id": fake_data.random_int(1,10)}, 200
    response = app.test_client().post("/routes", json=data, headers={"Authorization": f'Bearer {token}'})
    response_info= json.loads(response.data.decode('utf-8'))
    assert response.status_code == 400
 
@patch('project.views.get_token')
def test_crear_trayecto_sourceAirportCode_formato_invalido400(mock_token):

    data = 	{
        "sourceAirportCode": fake_data.word(ext_word_list=["ABFK", "JHIP", "LKOC", "IJHY", "HGYW", "LLOJ", "WODB","PLSX"]),
        "destinyAirportCode": fake_data.word(ext_word_list=["ABF", "JHI", "LKO", "IJH", "HGY", "LLO", "WOD","PLS"]),
        "destinyCountry": fake_data.word(),
        "bagCost": 0,
        "sourceCountry": fake_data.word()
    }

    token = "iisjsu"
    
    # crear trayecto
    mock_token.return_value = {"user_id": fake_data.random_int(1,10)}, 200
    response = app.test_client().post("/routes", json=data, headers={"Authorization": f'Bearer {token}'})
    response_info= json.loads(response.data.decode('utf-8'))
    assert response.status_code == 400
 
@patch('project.views.get_token')
def test_crear_trayecto_destinyAirportCode_formato_invalido_400(mock_token):

    data = 	{
        "sourceAirportCode": fake_data.word(ext_word_list=["ABF", "JHI", "LKO", "IJH", "HGY", "LLO", "WOD","PLS"]),
        "destinyAirportCode": fake_data.word(ext_word_list=["ABFI", "JHIP", "LKOC", "IJHV", "HGYN", "LLOG", "WODW","PLSO"]),
        "destinyCountry": fake_data.word(),
        "bagCost": 0,
        "sourceCountry": fake_data.word()
    }

    token = "iisjsu"
    
    # crear trayecto
    mock_token.return_value = {"user_id": fake_data.random_int(1,10)}, 200
    response = app.test_client().post("/routes", json=data, headers={"Authorization": f'Bearer {token}'})
    response_info= json.loads(response.data.decode('utf-8'))
    assert response.status_code == 400
 

@patch('project.views.get_token')
def test_obtener_trayecto_por_id_200(mock_token):

    data = 	{
        "sourceAirportCode": fake_data.word(ext_word_list=["ABF", "JHI", "LKO", "IJH", "HGY", "LLO", "WOD","PLS"]),
        "destinyAirportCode": fake_data.word(ext_word_list=["ABF", "JHI", "LKO", "IJH", "HGY", "LLO", "WOD","PLS"]),
        "destinyCountry": fake_data.word(),
        "bagCost": fake_data.random_int(10,600),
        "sourceCountry": fake_data.word()
    }

    token = "iisjsu"
    
    # crear trayecto
    mock_token.return_value = {"user_id": fake_data.random_int(1,10)}, 200
    response = app.test_client().post("/routes", json=data, headers={"Authorization": f'Bearer {token}'})
    response_info= json.loads(response.data.decode('utf-8'))
    assert response.status_code == 201
 

    # obtener project
    response = app.test_client().get("/routes/3", json=data, headers={"Authorization": f'Bearer {token}'})
    response_info= json.loads(response.data.decode('utf-8'))
    assert response.status_code == 200
    ids = [r['id'] for r in response_info]
    assert 3 in ids



@patch('project.views.get_token')
def test_obtener_trayecto_por_id_404(mock_token):


    token = "iisjsu"
    
    # crear trayecto
    mock_token.return_value = {"user_id": fake_data.random_int(1,10)}, 200

    # obtener project
    response = app.test_client().get("/routes/999999", headers={"Authorization": f'Bearer {token}'})
    response_info= json.loads(response.data.decode('utf-8'))
    assert response.status_code == 404
 

@patch('project.views.get_token')
def test_obtener_trayecto_por_parametro_when_200(mock_token):


    token = "iisjsu"
    

    mock_token.return_value = {"user_id": fake_data.random_int(1,10)}, 200

    date = datetime.date.today().isoformat()
    # obtener project
    response = app.test_client().get("/routes?when={}".format(date), headers={"Authorization": f'Bearer {token}'})
    response_info= json.loads(response.data.decode('utf-8'))

    assert response.status_code == 200

@patch('project.views.get_token')
def test_obtener_trayecto_por_parametro_to_200(mock_token):


    token = "iisjsu"
    

    mock_token.return_value = {"user_id": fake_data.random_int(1,10)}, 200

    date = datetime.date.today().isoformat()
    # obtener project
    response = app.test_client().get("/routes?to=ADF", headers={"Authorization": f'Bearer {token}'})
    response_info= json.loads(response.data.decode('utf-8'))
    assert response.status_code == 200


@patch('project.views.get_token')
def test_crear_trayecto_412(mock_token):
    
    data1 = 	{
        "sourceAirportCode": fake_data.word(ext_word_list=["ABF", "JHI", "LKO", "IJH", "HGY", "LLO", "WOD","PLS"]),
        "destinyAirportCode": fake_data.word(ext_word_list=["ABF", "JHI", "LKO", "IJH", "HGY", "LLO", "WOD","PLS"]),
        "destinyCountry": "Colombia",
        "bagCost": fake_data.random_int(10,600),
        "sourceCountry": "Peru"
    }

    token="abcdefg"
    
    mock_token.return_value = {"user_id": fake_data.random_int(1,10)}, 200
    response = app.test_client().post('/routes', json=data1, headers={"Authorization": f'Bearer {token}'})    
    response_info= json.loads(response.data.decode('utf-8'))
    assert response.status_code == 201
   # assert response_info[0]['id']== data['id']
   #  assert len(list(response_info.keys())) == 3

    data2 = 	{
        "sourceAirportCode": fake_data.word(ext_word_list=["ABF", "JHI", "LKO", "IJH", "HGY", "LLO", "WOD","PLS"]),
        "destinyAirportCode": fake_data.word(ext_word_list=["ABF", "JHI", "LKO", "IJH", "HGY", "LLO", "WOD","PLS"]),
        "destinyCountry": "Colombia",
        "bagCost": fake_data.random_int(10,600),
        "sourceCountry": "Peru"
    }

    response = app.test_client().post('/routes', json=data2, headers={"Authorization": f'Bearer {token}'})    
    response_info= json.loads(response.data.decode('utf-8'))
    assert response.status_code == 412



