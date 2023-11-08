from pydantic import BaseModel, Field
from typing import Optional, List


class Error400(BaseModel):
    message: str = Field("Bad Request", description='none')


class CreateProject(BaseModel):
    projectName: str = Field(..., description='email valid', example='mayhem')
    description: str = Field(..., description='password valid 8 caracteres', example='La primera regla del Club de la pelea es: nadie habla sobre el Club ...')
    companyId: str = Field(..., description='password valid 8 caracteres', example=1)


class CreateProjectResponse(BaseModel):
    message:  str = Field('Project projectName successfully created', description="name candidate")


RESPONSE_CREATEPROJECT = {
    200: CreateProjectResponse,
    400: Error400,
    }


class ProjectQuery(BaseModel):
    companyId: int = Field(..., description='Skills', example=1)


class ProjectResponse(BaseModel):
    root: CreateProject
    id: int = Field(1, description="last name candidate")
    status: str = Field('BASE', description="name candidate")
    createdAt: str = Field('2023-11-07T02:54:33.098514', description="name candidate")


RESPONSE_PROJECT = {
    200: ProjectResponse,
    400: Error400,
    }


class ProjectEmployeeAssociate(BaseModel):
    projectId: int = Field(..., description='Skills', example=1)
    employeeId: int = Field(..., description='Skills', example=1)


class ProjectEmployeeAssociateResponse(BaseModel):
    createdAt: str = Field('employee was link with the project', description="name candidate")


RESPONSE_PROJECT_EMPLOYEE = {
    200: ProjectEmployeeAssociateResponse,
    400: Error400,
    }
