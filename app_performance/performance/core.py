import requests
import json
from datetime import datetime
from .models import (
    Performance,
    db,
    PerformanceaSchema,
)
from .factory import get_project
from itertools import groupby
from operator import itemgetter
import logging


def make_evaluation_performance(request):
    metrics = json.dumps(
        {"communication": "80/100",
         "company values": "80/100",
         "leadership": "70/100",
         "overall performance": "60/100"
         }
    )
    feedback = 'good job'
    try:
        performance_details = Performance.query.filter(
            Performance.id == request.json["performanceId"]).first()

        if performance_details is None:
            return {"message": "interview not found"}, 404

        performance_details.score = request.json["score"]
        performance_details.employeeId = request.json.get('employeeId', 0),
        performance_details.feedback = feedback,
        performance_details.metrics = metrics
        db.session.commit()

        return {"message": "Performance successfully",
                "id": performance_details.id,
                "createdAt": datetime.now().isoformat()
                }, 200
    except Exception as e:
        print(e)
        return {"message": f"Missing: {e}"}, 400


def get_performance(request):
    projectsSchema = PerformanceaSchema()

    id_company = request.view_args.get('id_company', -1)
    id_candidate = request.view_args.get('id_candidate', -1)
    if id_company > 0:
        list_performance = Performance.query.filter(Performance.candidateId == id_candidate).all()
    else:
        list_performance = Performance.query.filter(Performance.companyId == id_company).all()

    projects_list = [projectsSchema.dump(performance) for performance in list_performance]
    [performance.update({"employees": json.loads(performance.get("employees"))})
        for performance in projects_list if performance.get("employees")]

    return projects_list, 200


def get_make_evaluation_performance(request):
    projectsSchema = PerformanceaSchema()
    id_company = request.view_args.get('id_company', -1)
    list_performance = Performance.query.filter(Performance.companyId == id_company).all()
    projectsList = [projectsSchema.dump(performance) for performance in list_performance]

    projectsList = sorted(projectsList,
                      key=itemgetter('projectId'))

    list_performance = []

    for key, value in groupby(projectsList,
                              key=itemgetter('projectId')):

        list_cand = []
        for info_proj in value:
            dic_cand = dict((k, info_proj[k]) for k in ('candidateId', 'candidate_name', "id",) if k in info_proj)
            list_cand.append(dic_cand)
        print(info_proj)
        logging.warning(f'PROJECT! {info_proj}')
        dict_project = {
            "projectId": key,
            'project_name': info_proj.get('project_name'),
            'candidateContract': list_cand,
            "project_employees_companie": json.loads(info_proj.get('employees')),
        }
        list_performance.append(dict_project)

    return list_performance, 200


def candidate_evaluate(request):
    companyId = request.json.get('companyId')
    projectId = request.json.get('projectId')
    candidateId = request.json.get('candidateId')
    data_proyect = get_project(companyId, projectId, candidateId)
    new_candidate_evaluate = Performance(
        candidateId=candidateId,
        projectId=projectId,
        companyId=companyId,
        candidate_name=data_proyect.get('candidateName', 'none'),
        project_name=data_proyect.get('projectName', 'none'),
        company_name=data_proyect.get('companyName', 'none'),
        employees=json.dumps(data_proyect.get('project_employees_companie', 'none')),
    )
    db.session.add(new_candidate_evaluate)
    db.session.commit()
    return {"message": "Candidate created for performance"}, 200