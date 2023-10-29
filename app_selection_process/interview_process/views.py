import os
from flask import Blueprint, request
from flask import send_from_directory
from .core import *
from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint


interviews_tag = Tag(name="interviews", description="manage inteviews")
interviews = APIBlueprint('interviews', __name__,url_prefix='/interviews')


@interviews.post("/", tags=[interviews_tag])
def create_interview():

    '''
    Company can create interviews
    :return: response
    '''
    
    response, status = create_company_interview(request)
    return response, status

@interviews.get("/company/<int:id_company>", tags=[interviews_tag])
def get_interviewsCompany():

    '''
    Company can get all its interviews
    :return: response
    '''
    response, status = get_company_interviews(request)
    return response, status

@interviews.get("/candidate/<int:id_candidate>", tags=[interviews_tag])
def get_interviewsCandidate():

    '''
    Candidate can get all their interviews
    :return: response
    '''
    response, status = get_candidate_interviews(request)
    return response, status

@interviews.post("/score/<int:id_interview>", tags=[interviews_tag])
def interview_score():

    '''
    Company can evaluate interviews
    :return: response
    '''
    
    response, status = evaluate_company_interview(request)
    return response, status


@interviews.get('/ping', tags=[interviews_tag])
def root():
    '''
    Healt Check
    :return: pong
    '''
    return 'pong'


@interviews.get('/ping2', tags=[interviews_tag])
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