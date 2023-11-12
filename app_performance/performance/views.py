import os
from flask import request
from flask import send_from_directory
from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint
from .core import (
    make_evaluation_performance
)
from .serializer import (
    MakeEvaluation,
    RESPONSE_MAKEEVALUATION,
)

performance = APIBlueprint('performan', __name__, url_prefix='/performance')

performance_tag = Tag(name="Performance", description="Some Performance")

@performance.post("/make-evaluation",  tags=[performance_tag], responses=RESPONSE_MAKEEVALUATION)
def make_evaluation(body: MakeEvaluation):
    """
    user Performance can do a acount
    :return: response, status
    """
    response, status = make_evaluation_performance(request)
    return response, status


@performance.get("/evaluation/company",  tags=[performance_tag])
def get_evaluations_company():
    """
    user Performance can do a acount
    :return: response, status
    """
    response, status = {}, 200
    return response, status


@performance.get("/evaluation/candidate",  tags=[performance_tag], )
def get_evaluations_candiate():
    """
    user Performance can do a acount
    :return: response, status
    """
    response, status = {}, 200
    return response, status


@performance.post("/employee-evaluator", tags=[performance_tag])
def employee_evaluator():
    """
    user Performan can
    :return: response, status
    """
    response, status = {}, 200
    return response, status


performance_health_tag = Tag(name="Performance healtcheck", description="Some Performan")


@performance.get('/ping', tags=[performance_health_tag])
def root():
    """
    Healt Check
    :return: pong
    """
    return 'pong'


@performance.get('/ping2', tags=[performance_health_tag])
def ping():
    username = os.getenv('SQLALCHEMY_DATABASE_URI', 'admin')
    return f'pong12 {username}'


@performance.route('/coverage')
def coverage_app():
    os.system('pytest --cov --cov-report=html:template')
    return send_from_directory('./template/', 'index.html')


@performance.route('/<path>/')
def coverage_app_files(path):
    return send_from_directory('./template/', path)