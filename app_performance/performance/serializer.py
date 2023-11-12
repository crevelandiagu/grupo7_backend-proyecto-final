from pydantic import BaseModel, Field
from typing import Optional, List


class SearchPath(BaseModel):
    id_candidate: int = Field(..., description='Candidate id', example=1)


class Error400(BaseModel):
    message: str = Field("Bad Request", description='none')


class MakeEvaluation(BaseModel):
    candidateId: int = Field(..., description='candidate Id ', example=1)
    companyId: int = Field(..., description='company Id', example=1)
    projectId: int = Field(..., description='project Id', example=1)
    employeeId: int = Field(None, description='employee Id', example=1)
    score: int = Field(..., description='score', example=1)


class MakeEvaluationResponse(BaseModel):
    message:  str = Field('Performance successfully added', description="name candidate")
    id:  int = Field(1, description="last name candidate")
    createdAt:  str = Field('2023-11-07T02:54:33.098514', description="years experience candidate")


RESPONSE_MAKEEVALUATION = {
    200: MakeEvaluationResponse,
    400: Error400,
    }


class LogInResponse(BaseModel):
    id: int = Field(1, description="last name candidate")
    message:  str = Field("Inicio de sesión exitoso", description="name candidate")
    token: str = Field('token', description="name candidate")


RESPONSE_LOGIN = {
    200: LogInResponse,
    400: Error400,
    }


class BasicInfo(BaseModel):
    name: str = Field(None, description='email valid', example='usertest')
    lastname: str = Field(None, description='email valid', example='test2')
    birthdate: str = Field(None, description='email valid', example='01/01/1999')
    nacionality: str = Field(None, description='email valid', example='COL')
    phone_number: str = Field(None, description='email valid', example='123456789')
    numberId: str = Field(None, description='email valid', example='C.C.123456789')


class BasicInfoResponse(BasicInfo):
    email:  str = Field('usertest@gmail.com', description='email valid')
    initialLatter: str = Field("UT", description='email valid')
    full_name:  str = Field('usertest test2', description='email valid')


RESPONSE_BASICINFO = {
    200: BasicInfoResponse,
    400: Error400,
    }


class BasicInfoExperience(BaseModel):
    position: str = Field(None, description='email valid', example='Junior')
    company_name: str = Field(None, description='email valid', example='MIT')
    start_date: str = Field(None, description='email valid', example='01/01/1999')
    end_date: str = Field(None, description='email valid', example='01/12/1999')
    place: str = Field(None, description='email valid', example='COL')
    skills: str = Field(None, description='email valid', example='["Python", "Java"]')


class BasicInfoExperienceResponse(BaseModel):
    __root__: List[BasicInfoExperience]

