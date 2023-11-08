import secrets
import hashlib
from .models import Interview, db, InterviewSchema
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from datetime import datetime

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

    newInterview = Interview(
        date_interview=interview_date,
        candidate_name=candidate_name,
        candidate_id=candidate_id,
        company_id=company_id,
        company_employee_id=company_employee_id,
        project_id=project_id,
        status=interview_status
    )
    try:
        db.session.add(newInterview)
        db.session.commit()
    except Exception as e:
        print(e)
        return {"message": "Internal server error"}, 500
    
    return {"message": f"Interview successfully created"}, 200


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
        print(e)
        return {"message": "Wrong score format"}, 412

    try:

        interview_details = Interview.query.filter(Interview.id == interviewId).first()
        
        if interview_details is None:
            return {"message": "interview not found"}, 404
        
        interview_details.score = data_score
        db.session.commit()
        return interviewSchema.dump(interview_details), 200

    except Exception as e:
        print(e)
        return {"message": f"missing {e}"}, 400