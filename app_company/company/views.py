import os
from flask import Blueprint
from flask import request
from flask import send_from_directory
from .core import (creacion_usuario,
                   autenticar_usuario,
                   build_basicinfo)
from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint
from .serializer import (
    SignUp,
    RESPONSE_SIGNUP,
    RESPONSE_LOGIN,
    RESPONSE_INFO,
    RESPONSE_BASICINFO,
    SearchPath,
    BasicInfo
)

company = APIBlueprint('company', __name__, url_prefix='/company')

company_tag = Tag(name="company", description="Some company")

@company.post("/signup",  tags=[company_tag], responses=RESPONSE_SIGNUP)
def register_users(body: SignUp):
    """
    user company can do a acount
    :return: response, status
    """
    response, status = creacion_usuario(request)
    return response, status


@company.post("/login", tags=[company_tag], responses=RESPONSE_LOGIN)
def information_user(body: SignUp):
    """
    user company can login
    :return: response, status
    """
    response, status = autenticar_usuario(request)
    return response, status


@company.get("/profile/basicinfo/<int:id_company>/", tags=[company_tag], responses=RESPONSE_INFO)
def get_basic_info_user(path: SearchPath):
    response, status = build_basicinfo(request)
    return response, status


@company.post("/profile/basicinfo/<int:id_company>/", tags=[company_tag], responses=RESPONSE_BASICINFO)
def post_basic_info_user(body: BasicInfo, path: SearchPath):
    response, status = build_basicinfo(request)
    return response, status


company_health_tag = Tag(name="Company healtcheck", description="Some company")


@company.get('/ping', tags=[company_health_tag])
def root():
    """
    Healt Check
    :return: pong
    """
    return 'pong'


@company.get('/ping2', tags=[company_health_tag])
def ping():
    username = os.getenv('SQLALCHEMY_DATABASE_URI', 'admin')
    return f'pong12 {username}'


@company.route('/coverage')
def coverage_app():
    os.system('pytest --cov --cov-report=html:template')
    return send_from_directory('./template/', 'index.html')


@company.route('/<path>/')
def coverage_app_files(path):
    return send_from_directory('./template/', path)