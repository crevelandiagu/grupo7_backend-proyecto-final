import os
from flask import Blueprint, request
from flask import send_from_directory
from .core import *
from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint
from .serializer import (
    CreateCompanyInterview,
    RESPONSE_CREATE_INTERVIEW,
    CompanyInterviewPath,
    RESPONSE_INTERVIEW,
    CandidateInterviewPath,
    EvaluateInterviewPath,
    EvaluateInterview,
    RESPONSE_EVALUATE_INTERVIEW,
    CreateContract
)

interviews = APIBlueprint('interviews', __name__, url_prefix='/interviews')

interviews_tag = Tag(name="interviews", description="manage inteviews")


@interviews.post("/", tags=[interviews_tag], responses=RESPONSE_CREATE_INTERVIEW)
def create_interview(body: CreateCompanyInterview):
    """
    Company can create interviews
    :return: response
    """
    
    response, status = create_company_interview(request)
    return response, status


@interviews.get("/company/<int:id_company>", tags=[interviews_tag], responses=RESPONSE_INTERVIEW)
def get_interviews_company(path: CompanyInterviewPath):
    """
    Company can get all its interviews
    :return: response
    """
    response, status = get_company_interviews(request)
    return response, status


@interviews.get("/candidate/<int:id_candidate>", tags=[interviews_tag], responses=RESPONSE_INTERVIEW)
def get_interviews_candidate(path: CandidateInterviewPath):
    """
    Candidate can get all their interviews
    :return: response
    """
    
    response, status = get_candidate_interviews(request)
    return response, status


@interviews.post("/score/<int:id_interview>", tags=[interviews_tag], responses=RESPONSE_EVALUATE_INTERVIEW)
def interview_score(path: EvaluateInterviewPath, body: EvaluateInterview):
    """
    Company can evaluate interviews
    :return: response
    """
    
    response, status = evaluate_company_interview(request)
    return response, status


selection_process = APIBlueprint('selection process', __name__, url_prefix='/selection-process')

selection_process_tag = Tag(name="selection process", description="manage selection process")


@selection_process.get("/company/<int:id_company>", tags=[selection_process_tag], responses=RESPONSE_INTERVIEW)
def get_selection_process_company(path: CompanyInterviewPath):
    """
    Candidate can get all their interviews
    :return: response
    """

    response, status = get_selection_process(request)
    return response, status


@selection_process.post("/sign-contract/", tags=[selection_process_tag])
def post_sign_contract_process(body: CreateContract):
    """
    Candidate can get all their interviews
    :return: response
    """

    response, status = sign_contract_process(request)
    return response, status


@selection_process.post("/stop-process/", tags=[selection_process_tag])
def post_stop_process(body: CreateContract):
    """
    Do not continue with the process
    :return: response
    """

    response, status = stop_process(request)
    return response, status


interviews_health_tag = Tag(name="Interviews healtcheck", description="Some interviews")


@interviews.get('/ping', tags=[interviews_health_tag])
def root():
    """
    Healt Check
    :return: pong
    """
    return 'pong'


@interviews.get('/ping2', tags=[interviews_health_tag])
def ping():
    username = os.getenv('SQLALCHEMY_DATABASE_URI', 'admin')
    return f'pong11 {username}'


@interviews.route('/coverage')
def coverage_app():
    os.system('pytest --cov --cov-report=html:template')
    return send_from_directory('./template/', 'index.html')


@interviews.route('/<path>/')
def coverage_app_files(path):
    return send_from_directory('./template/', path)