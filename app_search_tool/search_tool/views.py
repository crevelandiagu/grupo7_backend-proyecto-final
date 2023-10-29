import os
import time
from flask import Blueprint
from flask import request
from flask import send_from_directory

from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint
from .search_args import get_dandidate
from .search_cv import get_cv_candidate


search_tool = APIBlueprint('search_tool', __name__, url_prefix='/search-tool')

search_tool_tag = Tag(name="Search Tool", description="Search candidate")


@search_tool.get("/search", tags=[search_tool_tag])
def get_candidate():
    response, status = get_dandidate(request)
    return response, status


@search_tool.get("/search/cv/<int:id_candidate>", tags=[search_tool_tag])
def get_candidate_cv():
    response, status = get_cv_candidate(request)
    return response, status


search_tool_health_tag = Tag(name="Search Tool healtcheck", description="Search Tool candidate")


@search_tool.get('/ping', tags=[search_tool_health_tag])
def root():
    '''
    Healt Check
    :return: pong
    '''

    return 'pong'


@search_tool.get('/ping2', tags=[search_tool_health_tag])
def ping():
    username = os.getenv('SQLALCHEMY_DATABASE_URI', 'admin')
    return f'pong12 {username}'


@search_tool.route('/coverage')
def coverage_app():
    os.system('pytest --cov --cov-report=html:template')
    return send_from_directory('./template/', 'index.html')


@search_tool.route('/<path>/')
def coverage_app_files(path):
    return send_from_directory('./template/', path)



