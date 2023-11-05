# from pydantic import BaseModel, Field
# from typing import Optional, List
#
#
# class Error400(BaseModel):
#     messeje: str = Field("Bad Request", description='none')
#
#
# class SearchQuery(BaseModel):
#     skill: Optional[str] = Field(None, description='Skills', example='Python-Java')
#     experienceYears: Optional[float] = Field(None, description='Experience Years', example=1)
#
#
# class SearchResponse(BaseModel):
#     name:  str = Field('name', description="name candidate")
#     lastName:  str = Field('last_name', description="last name candidate")
#     skills:  list = Field(['Python', 'Java'], description="skills candidate")
#     years_exp:  float = Field(1, description="years experience candidate")
#     candidateId:  int = Field(0, description="id candidate")
#
#
# class SearchResponseList(BaseModel):
#     __root__: List[SearchResponse]
#
#
# RESPONSE_SEARCH = {
#     200: SearchResponseList,
#     400: Error400,
#     }
#
#
# class SearchPath(BaseModel):
#     id_candidate: int = Field(..., description='Candidate id', example=1)
#
#
# class SearchResponseCv(BaseModel):
#
#     basicinfo:  dict = Field({
#         "email": "a@gmail.com",
#         "full_name": "Amanda Jacobs Silva",
#         "initial_latter": "AS",
#         "lastname": "Silva",
#         "nacionality": "Diazside",
#         "name": "Amanda Jacobs",
#         "phone_number": "799.617.2758x53565"
#     }, description="Basic information candidate")
#
#
#
#
# RESPONSE_SEARCH_CV = {
#     200: SearchResponseCv,
#     400: Error400,
#     }