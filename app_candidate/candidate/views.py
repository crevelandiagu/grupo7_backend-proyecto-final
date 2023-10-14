import os
from flask import Blueprint
from flask import request
from flask import send_from_directory
from .core import (creacion_usuario,
                   autenticar_usuario,
                   self_information)
from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint


candidate_tag = Tag(name="candidate", description="Some candidate")
candidate = APIBlueprint('candidate', __name__, url_prefix='/candidate')


@candidate.post("/signup", tags=[candidate_tag])
def register_users():
    '''
    User can register
    :return: response
    '''
    response, status = creacion_usuario(request)
    return response, status


@candidate.post("/login", tags=[candidate_tag])
def information_user():
    response, status = autenticar_usuario(request)
    return response, status


@candidate.get("/profile", tags=[candidate_tag])
def get_token_user():
    response, status = {}, 200
    return response, status


@candidate.post("/profile", tags=[candidate_tag])
def post_token_user():
    response, status = {}, 200
    return response, status


@candidate.get('/ping', tags=[candidate_tag])
def root():
    return 'pong'


@candidate.get('/ping2', tags=[candidate_tag])
def ping():
    username = os.getenv('SQLALCHEMY_DATABASE_URI', 'admin')
    return f'pong11 {username}'


@candidate.route('/coverage')
def coverage_app():
    return send_from_directory('./template/', 'index.html')


@candidate.route('/<path>/')
def coverage_app_files(path):
    return send_from_directory('./template/', path)