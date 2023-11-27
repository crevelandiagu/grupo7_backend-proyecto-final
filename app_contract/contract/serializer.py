from pydantic import BaseModel, Field
from typing import Optional, List


class SearchPathCandidate(BaseModel):
    id_candidate: int = Field(..., description='Candidate id', example=1)


class SearchPathCompany(BaseModel):
    id_company: int = Field(..., description='Company id', example=1)


class Error400(BaseModel):
    message: str = Field("Bad Request", description='none')


class SignContracResponse(BaseModel):
    message:  str = Field("The contract was signed successfully", description="name candidate")


RESPONSE_SIGN = {
    200: SignContracResponse,
    400: Error400,
    }

class CreateContract(BaseModel):
    candidateId: int = Field(..., description='candidateId', example=1)
    projectId: int = Field(..., description='projectId valid', example=1)
    companyId: int = Field(..., description='companyId valid', example=1)


