import os
import time
from flask import Blueprint
from flask import request
from flask import send_from_directory

from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint
from .search_args import get_dandidate
from .search_cv import get_cv_candidate
from .start_process import chosen_one_candidate
from .serializer import (
    SearchQuery,
    RESPONSE_SEARCH,
    SearchPath,
    RESPONSE_SEARCH_CV,
    ProjectChosenOne,
    RESPONSE_CHOSEN_ONE
)

search_tool = APIBlueprint('search_tool', __name__, url_prefix='/search-tool')

search_tool_tag = Tag(name="Search Tool", description="Search candidate")


@search_tool.get("/search", tags=[search_tool_tag], responses=RESPONSE_SEARCH)
def get_candidate(query: SearchQuery):
    response, status = get_dandidate(query)
    return response, status


@search_tool.get("/search/cv/<int:id_candidate>", tags=[search_tool_tag], responses=RESPONSE_SEARCH_CV)
def get_candidate_cv(path: SearchPath):
    print(path)
    response, status = get_cv_candidate(request)
    return response, status


@search_tool.post("/search/cv/chosen-one", tags=[search_tool_tag], responses=RESPONSE_CHOSEN_ONE)
def post_candidate_chosen_one(body: ProjectChosenOne):
    response, status = chosen_one_candidate(request)
    return response, status


search_tool_health_tag = Tag(name="Search Tool healtcheck", description="Search Tool candidate")


@search_tool.get('/ping', tags=[search_tool_health_tag])
def root():
    """
    Healt Check
    :return: pong
    """
    return 'pong'


@search_tool.get('/ping2', tags=[search_tool_health_tag])
def ping():
    """
    Get ping health check
    """
    username = os.getenv('SQLALCHEMY_DATABASE_URI', 'admin')
    return f'pong12 {username}'


@search_tool.route('/coverage')
def coverage_app():
    return send_from_directory('./template/', 'index.html')


@search_tool.route('/<path>/')
def coverage_app_files(path):
    return send_from_directory('./template/', path)



