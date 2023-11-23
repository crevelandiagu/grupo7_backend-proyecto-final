import os
from flask import Blueprint, request
from flask import send_from_directory
from .core import *
from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint
from .serializer import (
    SearchPathCandidate,
    SearchPathCompany,
    RESPONSE_SIGN
)

sign_contract = APIBlueprint('Contract', __name__, url_prefix='/contracts')

sign_contract_tag = Tag(name="Contract", description="manage Contract")


@sign_contract.post("/company/<int:id_company>", tags=[sign_contract_tag], responses=RESPONSE_SIGN)
def sign_contract_company(path: SearchPathCompany):
    """
    Company can create interviews
    :return: response
    """

    response, status = sign_contract_user(request)
    return response, status


@sign_contract.get("/company/<int:id_company>", tags=[sign_contract_tag], )
def get_contract_text_company(path: SearchPathCompany):
    """
    Company can get all its interviews
    :return: response
    """
    response, status = get_contract_text(request)
    return response, status


@sign_contract.post("/candidate/<int:id_candidate>", tags=[sign_contract_tag],responses=RESPONSE_SIGN)
def sign_contract_candidate(path: SearchPathCandidate):
    """
    Company can create interviews
    :return: response
    """

    response, status = sign_contract_user(request)
    return response, status


@sign_contract.get("/candidate/<int:id_candidate>", tags=[sign_contract_tag], )
def get_contract_text_candidate(path: SearchPathCandidate):
    """
    Company can get all its interviews
    :return: response
    """
    response, status = get_contract_text(request)
    return response, status


sign_contract_health_tag = Tag(name="Contract healtcheck", description="Some Contract")


@sign_contract.get('/ping', tags=[sign_contract_health_tag])
def root():
    """
    Healt Check
    :return: pong
    """
    return 'pong'


@sign_contract.get('/ping2', tags=[sign_contract_health_tag])
def ping():
    username = os.getenv('SQLALCHEMY_DATABASE_URI', 'admin')
    return f'pong11 {username}'


