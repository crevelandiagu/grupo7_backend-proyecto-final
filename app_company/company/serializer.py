from pydantic import BaseModel, Field
from typing import Optional, List


class Error400(BaseModel):
    message: str = Field("Bad Request", description='none')


class SearchPath(BaseModel):
    id_company: int = Field(..., description='company id', example=1)


class SignUp(BaseModel):
    email: str = Field(..., description='email valid', example='company_test@gmail.com')
    password: str = Field(..., description='password valid 8 caracteres', example='Adec123^&*ede#')


class SignUpResponse(BaseModel):
    message:  str = Field('User successfully added', description="name candidate")
    id:  int = Field(1, description="last name candidate")
    email:  str = Field('usertest@gmail.com', description="skills candidate")
    createdAt:  str = Field('2023-11-07T02:54:33.098514', description="years experience candidate")


RESPONSE_SIGNUP = {
    200: SignUpResponse,
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
    name: str = Field(None, description='email valid', example='company usertest')
    nit: str = Field(None, description='email valid', example='123456789')
    number_employees: str = Field(None, description='email valid', example='20')
    core: str = Field(None, description='email valid', example='browser')
    senority: str = Field(None, description='email valid', example='3')


RESPONSE_INFO = {
    200: BasicInfo,
    400: Error400,
    }


class InfoCreateResponse(BaseModel):
    message: str = Field("Company add info basic successfully", description='none')


RESPONSE_BASICINFO = {
    200: InfoCreateResponse,
    400: Error400,
    }
