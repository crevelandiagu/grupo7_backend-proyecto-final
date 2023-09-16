from flask import Blueprint
from flask import request
import os
from .core import get_token, create_post_, search_post_, get_post_


publicaciones = Blueprint('company_employees', __name__)

users_ip = os.getenv('USERS_URL', "http://127.0.0.1:3000")
user_port = os.getenv('USER_PORT',"3000")
user_endpoint = os.getenv('USER_ENDPOINT',"/app_company/me")

@publicaciones.route('/posts/', methods=['POST'])
def create_post():
    headers=request.headers
    user, status_header = get_token(headers,users_ip, user_port, user_endpoint)

    if status_header != 200:
        return "El token no es válido o está vencido.", 401
    response, status = create_post_(request, user)
    return  response, status
    
@publicaciones.route('/posts/', methods=['GET'] )
def search_post():
    headers=request.headers
    user, status_header = get_token(headers,users_ip, user_port, user_endpoint)
    
    if status_header != 200:
        return "El token no es válido o está vencido.", 401
    response, status = search_post_(request, user)
    return  response, status

@publicaciones.route('/posts/<id>', methods=['GET'] )
def get_post(id):
    headers=request.headers
    response_header, status_header = get_token(headers,users_ip, user_port, user_endpoint)

    if status_header != 200:
        return "El token no es válido o está vencido.", 401
    try:
        id_post = int(id)
    except Exception as e:
        return {"mensaje": f"Id de post invalido, no es un numero"}, 400
    
    response, status = get_post_(id_post, response_header)
    return response, status


@publicaciones.route('/posts/ping', )
def ping():
    return 'pong'



