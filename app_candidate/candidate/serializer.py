from pydantic import BaseModel, Field
from typing import Optional, List


class SearchPath(BaseModel):
    id_candidate: int = Field(..., description='Candidate id', example=1)


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


RESPONSE_BASICINFO_EXPERIENCE = {
    200: BasicInfoExperienceResponse,
    400: Error400,
    }


class BasicInfoEducation(BaseModel):
    university: str = Field(None, description='email valid', example='MIT')
    subject: str = Field(None, description='email valid', example='Computer Science')
    start_date: str = Field(None, description='email valid', example='01/01/1999')
    end_date: str = Field(None, description='email valid', example='01/12/1999')
    skills: str = Field(None, description='email valid', example='["Python", "Java"]')


class BasicInfooEducationResponse(BaseModel):
    __root__: List[BasicInfoEducation]


RESPONSE_BASICINFO_EDUCATION = {
    200: BasicInfooEducationResponse,
    400: Error400,
    }


class BasicInfoCertificates(BaseModel):
    name_certificate: str = Field(None, description='email valid', example='OOP')
    company: str = Field(None, description='email valid', example='MIT')
    expedition_date: str = Field(None, description='email valid', example='01/01/1999')
    date_expiry: str = Field(None, description='email valid', example='01/12/1999')

class BasicInfoCertificatesResponse(BaseModel):
    __root__: List[BasicInfoCertificates]


RESPONSE_BASICINFO_CERTIFICATES = {
    200: BasicInfoCertificatesResponse,
    400: Error400,
    }

class CvInfoCreateResponse(BaseModel):
    message: str = Field("OK", description='none')


RESPONSE_BASICINFO_CV = {
    200: CvInfoCreateResponse,
    400: Error400,
    }

