from pydantic import BaseModel, Field
from typing import Optional, List


class Error400(BaseModel):
    message: str = Field("Bad Request", description='none')


class SignUp(BaseModel):
    email: str = Field(..., description='email valid', example='usertest@gmail.com')
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
