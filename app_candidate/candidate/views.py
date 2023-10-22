import os
import time
from flask import Blueprint
from flask import request
from flask import send_from_directory
from .core import (creacion_usuario,
                   autenticar_usuario,
                 )
from .curriculum_vitae import (build_basicinfo,
                               build_experience,
                               build_education,
                               build_certificates)
from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint



candidate = APIBlueprint('candidate', __name__, url_prefix='/candidate')

candidate_tag = Tag(name="Candidate auth", description="Some candidate")


@candidate.post("/signup", tags=[candidate_tag])
def register_users():
    '''
    candidate can register
    :return: response
    '''
    response, status = creacion_usuario(request)
    return response, status


@candidate.post("/login", tags=[candidate_tag])
def information_user():
    '''
    Candidate can login
    :return: respone
    '''
    response, status = autenticar_usuario(request)
    return response, status


candidate_cv_tag = Tag(name="Candidate CV", description="Some candidate")


@candidate.get("/profile/basicinfo/<int:id_candidate>/", tags=[candidate_cv_tag])
def get_basic_info_user():
    response, status = build_basicinfo(request)
    return response, status


@candidate.post("/profile/basicinfo/<int:id_candidate>/", tags=[candidate_cv_tag])
def post_basic_info_user():
    response, status = build_basicinfo(request)
    return response, status


@candidate.get("/profile/experience/<id_candidate>", tags=[candidate_cv_tag])
def get_experience_user():
    response, status = build_experience(request)
    return response, status


@candidate.post("/profile/experience/<id_candidate>", tags=[candidate_cv_tag])
def post_experience_user():
    response, status = build_experience(request)
    return response, status


@candidate.get("/profile/education/<id_candidate>", tags=[candidate_cv_tag])
def get_education_user():
    response, status = build_education(request)
    return response, status


@candidate.post("/profile/education/<id_candidate>", tags=[candidate_cv_tag])
def post_education_user():
    response, status = build_education(request)
    return response, status


@candidate.get("/profile/certificates/<id_candidate>", tags=[candidate_cv_tag])
def get_certificates_user():
    response, status = build_certificates(request)
    return response, status


@candidate.post("/profile/certificates/<id_candidate>", tags=[candidate_cv_tag])
def post_certificates_user():
    response, status = build_certificates(request)
    return response, status


candidate_health_tag = Tag(name="Candidate healtcheck", description="Some candidate")


@candidate.get('/ping', tags=[candidate_health_tag])
def root():
    '''
    Healt Check
    :return: pong
    '''
    return 'pong'


@candidate.get('/ping2', tags=[candidate_health_tag])
def ping():
    username = os.getenv('SQLALCHEMY_DATABASE_URI', 'admin')
    return f'pong12 {username}'


@candidate.route('/coverage')
def coverage_app():
    os.system('pytest --cov --cov-report=html:template')
    return send_from_directory('./template/', 'index.html')


@candidate.route('/<path>/')
def coverage_app_files(path):
    return send_from_directory('./template/', path)