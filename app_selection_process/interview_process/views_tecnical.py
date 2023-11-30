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

tecnical = APIBlueprint('tecnical', __name__, url_prefix='/assement')

tecnical_tag = Tag(name="tecnical", description="manage tecnical process")


@tecnical.post("/take-exam/<int:assementId>/candidate", tags=[tecnical_tag], responses=RESPONSE_TAKE_EXAM)
def post_take_exam(path: SearchPath, body: TakeExamCandidateBody):
    """
    Company can create interviews
    :return: response
    """
    
    response, status = take_exam_candidate(request)
    return response, status


@tecnical.get("/take-exam/<int:assementId>/candidate", tags=[tecnical_tag])
def get_take_exam(path: SearchPath):
    """
    Company can create interviews
    :return: response
    """

    response, status = get_exam_candidate(request)
    return response, status


@tecnical.get("/candidate/<int:id_candidate>", tags=[tecnical_tag],)
def get_assements_candidate(path: SearchPathCandidate):
    """
    Candidate can get all their interviews
    :return: response
    """
    response, status = get_candidate_assements(request)
    return response, status

