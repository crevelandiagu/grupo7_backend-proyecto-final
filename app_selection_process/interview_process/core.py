import os
import logging
import requests
from .models import Interview, db, InterviewSchema, SelectionProcess, SelectionProcessSchema
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from datetime import datetime
from .factory import get_project
from .utils_gcp.gcp_pub_sub import GCP


interviewSchema = InterviewSchema()


#@jwt_required
def create_company_interview(request):

    data_interview = dict(request.json)
    interview_dateTime = data_interview.get('dateTime', "")
    candidate_name = data_interview.get('candidateName', "")
    interview_status = data_interview.get('interviewStatus', "")


    try:
        date_format = '%Y-%m-%dT%H:%M:%S'
        interview_date = datetime.strptime(interview_dateTime,date_format)
    except Exception as e:
        return {"message": "Wrong dateTime format. It should be yyyy-mm-ddThh:mm:ss"}, 412

    try:
        candidate_id = int(data_interview.get('candidateId', ""))
        company_id = int(data_interview.get('companyId', ""))
        company_employee_id = int(data_interview.get('companyEmployeeId', ""))
        project_id = int(data_interview.get('projectId', ""))
    except Exception as e:
        return {"message": "Parameters candidateId, companyId, companyEmployeeId, projectId must be integer"}, 412
    data_proyect = get_project(companyId=company_id, projectId=project_id, candidateId=candidate_id)
    newInterview = Interview(
        date_interview=interview_date,
        company_employee_id=company_employee_id,
        status='Scheduled',
        candidate_id=candidate_id,
        candidate_name=data_proyect.get('candidateName', 'none'),
        project_id=project_id,
        project_name=data_proyect.get('projectName', 'none'),
        company_id=company_id,
        company_name=data_proyect.get('companyName', 'none'),
    )
    try:
        db.session.add(newInterview)
        db.session.commit()

        progress_status = SelectionProcess.query.filter(
            SelectionProcess.candidate_id == candidate_id).first()
        if progress_status:

            progress_status.pogress_status = "Technical Interview"
            db.session.commit()

    except Exception as e:
        print(e)
        return {"message": "Internal server error"}, 500
    
    return {"message": f"Interview successfully created"}, 201


#@jwt_required
def get_company_interviews(request):

    try:
        companyId = int(request.view_args.get('id_company', -1))
    except:
        return {"message": "Company Id missing"}, 400    
    
    try:
        companyInterviews = Interview.query.filter(Interview.company_id == companyId).all()
    except Exception as e:
        return {"message": "Internal server error"}, 500
    
    companyInterviewsList = [interviewSchema.dump(inter) for inter in companyInterviews]

    return companyInterviewsList, 200


#@jwt_required
def get_candidate_interviews(request):

    try:
        candidateId = int(request.view_args.get('id_candidate', -1))
    except:
        return {"message": "Candidate Id missing"}, 400    
    
    
    try:
        candidateInterviews = Interview.query.filter(Interview.candidate_id == candidateId).all()

    except Exception as e:

        return {"message": "Internal server error"}, 500
    
    candidateInterviewsList = [interviewSchema.dump(inter) for inter in candidateInterviews]

    return candidateInterviewsList, 200


#@jwt_required
def evaluate_company_interview(request):

    interviewId = int(request.view_args.get('id_interview', -1))
    data_interview = dict(request.json)
    
    try:
        data_score = int(data_interview.get("score"))
    except Exception as e:
        return {"message": "Wrong score format"}, 412

    try:

        interview_details = Interview.query.filter(Interview.id == interviewId).first()
        
        if interview_details is None:
            return {"message": "interview not found"}, 404

        approve = 'Approved' if data_score > 3 else "Rejected"

        interview_details.score = data_score
        interview_details.status = approve
        db.session.commit()

        progress_status = SelectionProcess.query.filter(
            SelectionProcess.candidate_id == interview_details.candidate_id).first()
        if progress_status:
            progress_status.score = data_score
            progress_status.pogress_status = approve
            db.session.commit()

        return interviewSchema.dump(interview_details), 201

    except Exception as e:
        print(e)
        return {"message": f"missing {e}"}, 400


def get_selection_process(request):
    companyId = int(request.view_args.get('id_company', -1))
    company_process = SelectionProcess.query.filter(SelectionProcess.company_id == companyId).all()

    company_process =[{
                                "id": inter.id,
                                'candidate_id': inter.candidate_id,
                                'candidate_name': inter.candidate_name,
                                'project_id': inter.project_id,
                                'project_name': inter.project_name,
                                'company_id': inter.company_id,
                                'company_name': inter.company_name,
                                'pogress_status': inter.pogress_status,
                                'score': inter.score
                                 } for inter in company_process]
    return company_process, 200



def sign_contract_process(request):

    data_proyect = get_project(
        companyId=request.json.get('companyId'),
        projectId=request.json.get('projectId'),
        candidateId=request.json.get('candidateId')
    )

    data = {
        "candidateId": request.json.get('candidateId'),
        "projectId": request.json.get('projectId'),
        "companyId": request.json.get('companyId'),
        "candidate_name": data_proyect.get('candidateName', 'none'),
        "project_name": data_proyect.get('projectName', 'none'),
        "company_name": data_proyect.get('companyName', 'none'),
    }


    CONTRACT_URI = os.getenv('CONTRACT_URI', "http://127.0.0.1:3003/")
    project_path_basicinfo = f"contracts/company/contract-made"
    url_contrac = f"{CONTRACT_URI}{project_path_basicinfo}"

    PERFORMANCE_URI = os.getenv('PERFORMANCE_URI', "http://127.0.0.1:3006/")
    performance_path_basicinfo = f"performance/candidate-evaluate"
    url_performance = f"{PERFORMANCE_URI}{performance_path_basicinfo}"
    try:
        requests.post(url=url_performance, json=data)
        response_token = requests.post(url=url_contrac, json=data)
        return response_token.json(), 200
    except Exception as e:
        return e, 401


def stop_process(request):
    message_start_process = {
        "where": "candidate-stop-process",
        "candidateId": request.json['candidateId'],
        "projectId": request.json['projectId'],
        "companyId": request.json['companyId'],
    }

    logging.warning(f'Watch! DELETE')
    try:
        logging.warning(f'Watch! send DELETE')
        publicar = GCP()
        publicar.publisher_message(message_start_process)
    except Exception as e:
        logging.warning(f'Watch! NO SEND {e}')
        print({"message": f"{e}"})
    return {"message": "The candidate does not continue in the process"}, 200

