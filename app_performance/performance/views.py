import os
from flask import request
from flask import send_from_directory
from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint
from .core import (
    make_evaluation_performance,
    get_performance,
    get_make_evaluation_performance,
    candidate_evaluate
)
from .serializer import (
    MakeEvaluation,
    RESPONSE_MAKEEVALUATION,
    SearchPathCandidate,
    RESPONSE_EVALUATION_GET,
    SearchPathCompany,
    RESPONSE_EVALUATION_GET_MAKE,
    BodyMakeEvaluation
)

performance = APIBlueprint('performan', __name__, url_prefix='/performance')

performance_tag = Tag(name="Performance", description="Some Performance")

@performance.post("/make-evaluation",  tags=[performance_tag], responses=RESPONSE_MAKEEVALUATION)
def make_evaluation(body: MakeEvaluation):
    """
    Do a performances for a candidate
    :return: response, status
    """
    response, status = make_evaluation_performance(request)
    return response, status


@performance.get("/make-evaluation/<int:id_company>",  tags=[performance_tag], responses=RESPONSE_EVALUATION_GET_MAKE)
def get_make_evaluation(path: SearchPathCompany):
    """
    Get all the candidates that can be performed
    :return: response, status
    """
    response, status = get_make_evaluation_performance(request)
    return response, status



@performance.get("/company/<int:id_company>/evaluation",  tags=[performance_tag], responses=RESPONSE_EVALUATION_GET)
def get_evaluations_company(path: SearchPathCompany):
    """
    Get all performances by do for a company
    :return: response, status
    """
    response, status = get_performance(request)
    return response, status


@performance.get("/candidate/<int:id_candidate>/evaluation",  tags=[performance_tag], responses=RESPONSE_EVALUATION_GET)
def get_evaluations_candiate(path: SearchPathCandidate):
    """
    Gets all the performances done for the candidates
    :return: response, status
    """
    response, status = get_performance(request)
    return response, status


@performance.post("/candidate-evaluate", tags=[performance_tag])
def post_candidate_evaluate(body: BodyMakeEvaluation):
    """
    Create the candidate when sign contract
    :return: response, status
    """
    response, status = candidate_evaluate(request)
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

