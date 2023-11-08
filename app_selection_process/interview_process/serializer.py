from pydantic import BaseModel, Field
from typing import Optional, List


class Error400(BaseModel):
    message: str = Field("Bad Request", description='none')


class CreateCompanyInterview(BaseModel):
    dateTime: str = Field(..., description='email valid', example='2023-01-01T12:12:12')
    candidateName: str = Field(..., description='password valid 8 caracteres', example='CandidateTest')
    interviewStatus: str = Field(..., description='password valid 8 caracteres', example='create')
    candidateId: str = Field(..., description='password valid 8 caracteres', example=1)
    companyId: str = Field(..., description='password valid 8 caracteres', example=1)
    companyEmployeeId: str = Field(..., description='password valid 8 caracteres', example=1)
    projectId: str = Field(..., description='password valid 8 caracteres', example=1)


class CreateCompanyInterviewResponse(BaseModel):
    message:  str = Field('Interview successfully created', description="name candidate")


RESPONSE_CREATE_INTERVIEW = {
    200: CreateCompanyInterviewResponse,
    400: Error400,
    }


class CompanyInterviewPath(BaseModel):
    id_company: int = Field(..., description='company id', example=1)


class CompanyInterview(BaseModel):
    id: int = Field(1, description='email valid')
    date_interview: str = Field('2023-01-01T12:12:12', description='email valid')
    candidate_name: str = Field('Candidate1', description='email valid')
    candidate_id: int = Field(1, description='email valid', )
    company_id: int = Field(1, description='email valid', )
    company_employee_id: int = Field(1, description='email valid', )
    score: int = Field(0, description='email valid', )
    project_id: int = Field(1, description='email valid',)
    status: str = Field('Interview', description='email valid', )
    createdAt: str = Field('2023-01-01T12:12:12', description='email valid',)


class CompanyInterviewsResponse(BaseModel):
    __root__: List[CompanyInterview]


RESPONSE_INTERVIEW = {
    200: CompanyInterviewsResponse,
    400: Error400,
    }


class CandidateInterviewPath(BaseModel):
    id_candidate: int = Field(..., description='candidate id', example=1)


class EvaluateInterviewPath(BaseModel):
    id_interview: int = Field(..., description='interview id', example=1)


class EvaluateInterview(BaseModel):
    score: int = Field(..., description='email valid', example=100)


RESPONSE_EVALUATE_INTERVIEW = {
    200: CompanyInterview,
    400: Error400,
    }
