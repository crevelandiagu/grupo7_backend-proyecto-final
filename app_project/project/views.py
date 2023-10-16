from flask import Blueprint, request
from .core import *
import os
from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint

# users_ip = os.getenv('USERS_URL', "http://127.0.0.1:3000")
# user_port = os.getenv('USER_PORT',"3000")
# user_endpoint = os.getenv('USER_ENDPOINT',"/app_company/me")

projects_tag = Tag(name="projects", description="manage projects")
projects = APIBlueprint("projects", __name__,url_prefix='/projects')


@projects.post("/createproject", tags=[projects_tag])
def create_project():

    #response, status = create_user_cv(request)
    #return response, status
    return "Ok", 201


@projects.get('/ping', tags=[projects_tag])
def root():
    '''
    Healt Check
    :return: pong
    '''
    return 'pong'


@projects.get('/ping2', tags=[projects_tag])
def ping():
    username = os.getenv('SQLALCHEMY_DATABASE_URI', 'admin')
    return f'pong11 {username}'


@projects.route('/coverage')
def coverage_app():
    return send_from_directory('./template/', 'index.html')


@projects.route('/<path>/')
def coverage_app_files(path):
    return send_from_directory('./template/', path)