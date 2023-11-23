import os
import requests

def request_app(url):

    try:
        response_token = requests.get(url=url)
    except Exception as e:
        return e, 401

    return response_token.json(), 200


def get_company(companyId):
    COMPANY_URI = os.getenv('COMPANY_URI', "http://127.0.0.1:3001/")
    company_path_basicinfo = f"company/profile/basicinfo/{companyId}"

    url_basicinfo = f"{COMPANY_URI}{company_path_basicinfo}"

    basicinfo, code_basicinfo = request_app(url_basicinfo)

    info_cv = {}
    if basicinfo and code_basicinfo == 200:
        info_cv['basicinfo'] = basicinfo

    return info_cv


def get_employees(companyId, employeeId):
    EMPLOYEE_URI = os.getenv('EMPLOYEE_URI', "http://127.0.0.1:3002/")
    employee_path_basicinfo = f"company-employees/employee/{employeeId}/company/{companyId}"

    url_basicinfo = f"{EMPLOYEE_URI}{employee_path_basicinfo}"

    basicinfo, code_basicinfo = request_app(url_basicinfo)

    info_cv = {}
    if basicinfo and code_basicinfo == 200:
        info_cv['basicinfo'] = basicinfo

    return info_cv