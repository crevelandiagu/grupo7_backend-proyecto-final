import os
import requests


def request_app(url):

    try:
        response_token = requests.get(url=url)
    except Exception as e:
        return e, 401

    return response_token.json(), 200


def get_project(companyId, projectId, candidateId):
    PROJECT_URI = os.getenv('PROJECT_URI', "http://127.0.0.1:3007/")
    project_path_basicinfo = f"projects/?companyId={companyId}"

    url_basicinfo = f"{PROJECT_URI}{project_path_basicinfo}"

    basicinfo, code_basicinfo = request_app(url_basicinfo)

    info_process = dict()
    if basicinfo and code_basicinfo == 200:
        for project in basicinfo:
            if int(project.get('id')) == int(projectId):
                info_process['projectName'] = project.get('projectName')
                info_process['companyName'] = project.get('companyData', {}).get("name", 'company_name')
                info_process['project_employees_companie'] = project.get('project_employees_companie', {})

                candidate_info = [i for i in project.get('candidate_project')
                                  if int(i.get('candidate_id')) == int(candidateId)]
                if candidate_info:
                    info_process['candidateName'] = candidate_info[0].get('full_name')

        return info_process

    return info_process
