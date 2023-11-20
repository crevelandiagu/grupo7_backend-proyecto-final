import os
from flask import Blueprint, request
from flask import send_from_directory
from .core_tecnical import *
from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint
from .serializer_tecnical import (
    TakeExamCandidateBody,
    RESPONSE_TAKE_EXAM,
    SearchPath,
    SearchPathCandidate
)

# assement/company/1
# assement/take-exam/1/candidate/

tecnical = APIBlueprint('tecnical', __name__,url_prefix='/assement')

tecnical_tag = Tag(name="tecnical", description="manage tecnical process")


@tecnical.post("/take-exam/<int:id_test>/candidate", tags=[tecnical_tag], responses=RESPONSE_TAKE_EXAM)
def take_exam(body: TakeExamCandidateBody, path:SearchPath):
    """
    Company can create interviews
    :return: response
    """
    
    response, status = take_exam_candidate(request)
    return response, status


@tecnical.get("/company/<int:id_company>", tags=[tecnical_tag], )
def get_interviews_company():
    """
    Company can get all its interviews
    :return: response
    """
    response, status = {}, 200
    return response, status


@tecnical.get("/candidate/<int:id_candidate>", tags=[tecnical_tag],)
def get_interviews_candidate(path: SearchPathCandidate):
    """
    Candidate can get all their interviews
    :return: response
    """
    
    response, status = get_candidate_assements(request)
    return response, status


@tecnical.post("/candidate/<int:id_candidate>", tags=[tecnical_tag], )
def create_candidate_assements():
    """
    Company can evaluate interviews
    :return: response
    """
    
    response, status = candidate_assements(request)
    return response, status


tecnical_health_tag = Tag(name="Tecnical healtcheck", description="Some tecnical")


@tecnical.get('/ping', tags=[tecnical_health_tag])
def root():
    """
    Healt Check
    :return: pong
    """
    return 'pong'


@tecnical.get('/ping2', tags=[tecnical_health_tag])
def ping():
    username = os.getenv('SQLALCHEMY_DATABASE_URI', 'admin')
    return f'pong11 {username}'
