import os
from flask import Blueprint
from flask import request
from flask import send_from_directory

from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint
from .core import (
    creacion_usuario,
    get_employees,
    get_employees_one
)
from .serializer import (
    CreateEmployee,
    RESPONSE_SIGNUP,
    SearchPath,
    RESPONSE_EMPLOYEE,
SearchPathOne
)

company_employees = APIBlueprint('company_employees', __name__, url_prefix='/company-employees')

company_employees_tag = Tag(name="Search Tool", description="Search candidate")


@company_employees.post('/create-employee/', tags=[company_employees_tag], responses=RESPONSE_SIGNUP)
def create_employe(body: CreateEmployee):
    '''
    candidate can register
    :return: response
    '''
    response, status = creacion_usuario(request)
    return response, status


@company_employees.get('/employee/<int:id_company>', tags=[company_employees_tag], responses=RESPONSE_EMPLOYEE)
def get_employes(path: SearchPath):
    '''
    candidate can register
    :return: response
    '''
    response, status = get_employees(request)
    return response, status


@company_employees.get('/employee/<int:id_employee>/company/<int:id_company>', tags=[company_employees_tag], responses=RESPONSE_EMPLOYEE)
def get_employe_company(path: SearchPathOne):
    '''
    candidate can register
    :return: response
    '''
    response, status = get_employees_one(request)
    return response, status

company_employees_health_tag = Tag(name="Search Tool healtcheck", description="Search Tool candidate")


@company_employees.get('/ping', tags=[company_employees_health_tag])
def root():
    '''
    Healt Check
    :return: pong
    '''
    return 'pong'


@company_employees.get('/ping2', tags=[company_employees_health_tag])
def ping():
    """
    Get ping health check
    """
    username = os.getenv('SQLALCHEMY_DATABASE_URI', 'admin')
    return f'pong12 {username}'


@company_employees.route('/coverage')
def coverage_app():
    os.system('pytest --cov --cov-report=html:template')
    return send_from_directory('./template/', 'index.html')


@company_employees.route('/<path>/')
def coverage_app_files(path):
    return send_from_directory('./template/', path)




