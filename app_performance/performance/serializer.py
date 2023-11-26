from pydantic import BaseModel, Field
from typing import Optional, List


class SearchPathCandidate(BaseModel):
    id_candidate: int = Field(..., description='Candidate id', example=1)


class SearchPathCompany(BaseModel):
    id_company: int = Field(..., description='company id', example=1)

class Error400(BaseModel):
    message: str = Field("Bad Request", description='none')


class MakeEvaluation(BaseModel):
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


class BodyMakeEvaluation(BaseModel):
    candidateId: int = Field(1, description="last name candidate")
    companyId: int = Field(1, description="last name candidate")
    projectId: int = Field(1, description="last name candidate")


class EvaluationAll(MakeEvaluation):
    candidateId: int = Field(1, description="last name candidate")
    candidate_name: str = Field("usertest test2", description="name candidate")
    companyId:int = Field(1, description="last name candidate")
    company_name: str = Field("company test", description="name candidate")

    employees: list = [{"companyId": 1, "companyProjectId": None, "email": "employeetest@gmail.com", "employeeId": 1}]

    projectId: int = Field(1, description="last name candidate")
    project_name: str = Field("mayhem", description="name candidate")


    createdAt:  str = Field("2023-11-13", description="name candidate")
    feedback:  str = Field("good job", description="name candidate")
    id: int = Field(1, description="last name candidate")
    metrics:  str = Field("{\"communication\": \"80/100\", \"company values\": \"80/100\", \"leadership\": \"70/100\", \"overall performance\": \"60/100\"}", description="name candidate")


class EvaluationAllResponse(BaseModel):
    __root__: List[EvaluationAll]


RESPONSE_EVALUATION_GET = {
    200: EvaluationAllResponse,
    400: Error400,
    }


class GetMakeEvaluation(MakeEvaluation):
    candidateContract:  list = Field([
      {
        "candidateId": 1,
        "candidate_name": "usertest test2",
        "id": 1
      }
    ], description="name candidate")
    projectId:  int = Field(1, description="name candidate")
    project_employees_companie: list = Field( [
      {
        "companyId": 1,
        "companyProjectId": None,
        "email": "employeetest@gmail.com",
        "employeeId": 1
      }
    ], description="last name candidate")
    project_name:  str = Field("mayhem", description="name candidate")


class GetMakeEvaluationResponse(BaseModel):
    __root__: List[GetMakeEvaluation]


RESPONSE_EVALUATION_GET_MAKE = {
    200: GetMakeEvaluationResponse,
    400: Error400,
    }
