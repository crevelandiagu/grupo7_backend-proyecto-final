import os
from flask import Blueprint, request
from flask import send_from_directory
from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint

from .core import (
    create_company_project,
    get_company_projects,
    associate_employee_projects
)

from .serializer import (
    CreateProject,
    RESPONSE_CREATEPROJECT,
    ProjectQuery,
    RESPONSE_PROJECT,
    ProjectEmployeeAssociate,
    RESPONSE_PROJECT_EMPLOYEE
)

projects = APIBlueprint("projects", __name__, url_prefix='/projects')

projects_tag = Tag(name="projects", description="manage projects")


@projects.post("/", tags=[projects_tag], responses=RESPONSE_CREATEPROJECT)
def create_project(body: CreateProject):
    """
    Company can create projects
    :return: response
    """
    response, status = create_company_project(request)
    return response, status


@projects.get("/", tags=[projects_tag], responses=RESPONSE_PROJECT)
def get_projects(query: ProjectQuery):
    """
    Company can get all its projects need companyId
    :return: response
    """
    response, status = get_company_projects(request)
    return response, status


@projects.post("/project-employe", tags=[projects_tag], responses=RESPONSE_PROJECT_EMPLOYEE)
def relate_projects_employee(body: ProjectEmployeeAssociate):
    """
    Company can link project and employee
    :return: response
    """
    response, status = associate_employee_projects(request)
    return response, status


projects_health_tag = Tag(name="Projects healtcheck", description="Some projects")


@projects.get('/ping', tags=[projects_health_tag])
def root():
    """
    Healt Check
    :return: pong
    """
    d = CandidateProject.delete().where(addresses_table.c.retired == 1)
    d.execute()
    return 'pong'


@projects.get('/ping2', tags=[projects_health_tag])
def ping():
    username = os.getenv('SQLALCHEMY_DATABASE_URI', 'admin')
    return f'pong11 {username}'


@projects.route('/coverage')
def coverage_app():
    os.system('pytest --cov --cov-report=html:template')
    return send_from_directory('./template/', 'index.html')


@projects.route('/<path>/')
def coverage_app_files(path):
    return send_from_directory('./template/', path)