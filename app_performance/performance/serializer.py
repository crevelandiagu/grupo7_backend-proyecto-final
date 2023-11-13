from pydantic import BaseModel, Field
from typing import Optional, List


class SearchPathCandidate(BaseModel):
    id_candidate: int = Field(..., description='Candidate id', example=1)


class SearchPathCompany(BaseModel):
    id_company: int = Field(..., description='company id', example=1)

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


class EvaluationAll(MakeEvaluation):
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
