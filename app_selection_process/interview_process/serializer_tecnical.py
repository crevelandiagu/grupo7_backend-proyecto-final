from pydantic import BaseModel, Field
from typing import Optional, List


class Error400(BaseModel):
    message: str = Field("Bad Request", description='none')


class SearchPath(BaseModel):
    assementId: int = Field(..., description='assement id', example=1)


class SearchPathCandidate(BaseModel):
    id_candidate: int = Field(..., description='candidate id', example=1)

class TakeExamCandidate(BaseModel):
    # [{id: 1, answer: "2"}]
    id: int = Field(..., description='email valid', example='1')
    answer: str = Field(..., description='password valid 8 caracteres', example='6')

class TakeExamCandidateBody(BaseModel):
    score: int = Field(30, description='email valid', example='30')
    # __root__: List[TakeExamCandidate]


class TakeExamCandidateResponse(BaseModel):
    score: int = Field(30, description='email valid', example='30')
    approve: bool = Field(True, description='password valid 8 caracteres', example='True')


RESPONSE_TAKE_EXAM = {
    200: TakeExamCandidateResponse,
    400: Error400,
    }


