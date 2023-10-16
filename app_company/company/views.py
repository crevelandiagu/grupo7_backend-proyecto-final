import os
from flask import Blueprint
from flask import request
from flask import send_from_directory
from .core import (creacion_usuario,
                   autenticar_usuario,
                   self_information)
from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint


company_tag = Tag(name="company", description="Some company")
company = APIBlueprint('company', __name__, url_prefix='/company')


@company.post("/singup",  tags=[company_tag])
def register_users():
    '''
    user company can do a acount
    :return: response, status
    '''
    response, status = creacion_usuario(request)
    return response, status


@company.post("/login", tags=[company_tag])
def information_user():
    '''
    :return:
    '''
    response, status = autenticar_usuario(request)
    return response, status


@company.get("/profile", tags=[company_tag])
def get_token_user():
    response, status = {}, 200
    return response, status


@company.post("/profile", tags=[company_tag])
def post_token_user():
    response, status = {}, 200
    return response, status


@company.get('/ping', tags=[company_tag])
def root():
    '''
    Healt Check
    :return: pong
    '''
    return 'pong'


@company.get('/ping2', tags=[company_tag])
def ping():
    username = os.getenv('SQLALCHEMY_DATABASE_URI', 'admin')
    return f'pong12 {username}'


@company.route('/coverage')
def coverage_app():
    return send_from_directory('./template/', 'index.html')


@company.route('/<path>/')
def coverage_app_files(path):
    return send_from_directory('./template/', path)