import os
import urllib3
import json


def endpoint_offers(headers,
                    method='GET',
                    ruta='app_performance/ping',
                    data={}):
    try:
        token = headers.get('Authorization').split(" ")[1]
    except Exception as e:
        return (401, 'token invalido')

    url_offers = os.getenv('OFFERS_URL', 'http://127.0.0.1:3003/')
    encoded_body = json.dumps(data)
    http = urllib3.PoolManager()
    response = http.request(method,
                            f'{url_offers}{ruta}',
                            body=encoded_body,
                            headers={"Authorization": f'Bearer {token}',
                                     'Content-Type': 'application/json'})
    try:
        return (response.status, json.loads(response.data.decode('utf-8')))
    except Exception as e:
        return (response.status, response.data.decode('utf-8'))

def endpoint_users(headers,
                   method='GET',
                   ruta='app_company/ping',
                   data={}):
    try:
        token = headers.get('Authorization').split(" ")[1]
    except Exception as e:
        return (401, 'token invalido')
    users_ip = os.getenv('USERS_URL', "http://127.0.0.1:3000/")
    encoded_body = json.dumps(data)
    http = urllib3.PoolManager()
    response = http.request(method,
                            f'{users_ip}{ruta}',
                            body=encoded_body,
                            headers={"Authorization": f'Bearer {token}',
                                     'Content-Type': 'application/json'})
    try:
        return (response.status, json.loads(response.data.decode('utf-8')))
    except Exception as e:
        return (response.status, response.data.decode('utf-8'))
    

def endpoint_posts(headers,
                    method='GET',
                    ruta='posts/ping',
                    data={}):

    try:
        token = headers.get('Authorization').split(" ")[1]
    except Exception as e:
        return (401, 'token invalido')

    url_posts = os.getenv('POSTS_URL', 'http://127.0.0.1:3001/')
    encoded_body = json.dumps(data)
    http = urllib3.PoolManager()
    response = http.request(method,
                            f'{url_posts}{ruta}',
                            body=encoded_body,
                            headers={"Authorization": f'Bearer {token}',
                                     'Content-Type': 'application/json'})

    try:
        return (response.status, json.loads(response.data.decode('utf-8')))
    except Exception as e:
        return (response.status, response.data.decode('utf-8'))



def endpoint_journey(headers,
                    method='GET',
                    ruta='routes/ping',
                    data={}):
    try:
        token = headers.get('Authorization').split(" ")[1]
    except Exception as e:
        return (401, 'token invalido')
    url_routes = os.getenv('ROUTES_URL', 'http://127.0.0.1:3002/')
    encoded_body = json.dumps(data)
    http = urllib3.PoolManager()
    response = http.request(method,
                            f'{url_routes}{ruta}',
                            body=encoded_body,
                            headers={"Authorization": f'Bearer {token}',
                                     'Content-Type': 'application/json'})
    try:
        return (response.status,  json.loads(response.data.decode('utf-8')))
    except Exception as e:
        return (response.status, response.data.decode('utf-8'))

