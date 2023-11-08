from pydantic import BaseModel, Field
from typing import Optional, List


class Error400(BaseModel):
    message: str = Field("Bad Request", description='none')


class CreateEmployee(BaseModel):
    email: str = Field(..., description='email valid', example='employeetest@gmail.com')
    password: str = Field(..., description='password valid 8 caracteres', example='Adec123^&*ede#')
    companyId: int = Field(..., description="last name candidate", example=1)


class CreateEmployeepResponse(BaseModel):
    message:  str = Field('User successfully added', description="name candidate")
    id:  int = Field(1, description="last name candidate")
    email:  str = Field('employeetest@gmail.com', description="skills candidate")
    createdAt:  str = Field('2023-11-07T02:54:33.098514', description="years experience candidate")


RESPONSE_SIGNUP = {
    200: CreateEmployeepResponse,
    400: Error400,
    }


class SearchPath(BaseModel):
    id_company: int = Field(..., description='Company id', example=1)


class Employee(BaseModel):
    employeeId: str = Field(1, description='email valid', example=1)
    email: str = Field('employeetest@gmail.com', description='email valid', example='employeetest@gmail.com')
    companyId: str = Field(1, description='email valid', example=1)
    companyProjectId: str = Field(1, description='email valid', example=1)


class EmployeeResponse(BaseModel):
    __root__: List[Employee]


RESPONSE_EMPLOYEE = {
    200: EmployeeResponse,
    400: Error400,
    }