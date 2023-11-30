
from .models import Assement, db, AssementSchema, SelectionProcess
from .exam import tecnical_test, logic_test


#@jwt_required
def take_exam_candidate(request):
    assementId = request.view_args.get('assementId', -1)
    info_cv_candidate = Assement.query.filter(Assement.id == assementId).first()
    id_test = info_cv_candidate.test_id

    dict_assement = {
        1: tecnical_test,
        2: logic_test
    }
    assement = dict_assement[id_test]
    score = 0
    if int(request.json.get("score", -1)) >= 0:
        score = int(request.json.get("score"))
    else:
        for answer in request.json:
            id = answer.get('id')
            result = assement[id]
            if answer.get('answer') == result.get('answer'):
                score += 1

    approve = 'Technical Interview' if score > 3 else "Rejected"

    info_cv_candidate.score = score
    info_cv_candidate.status = approve
    db.session.commit()

    progress_status = SelectionProcess.query.filter(
        SelectionProcess.candidate_id == info_cv_candidate.candidate_id).first()
    if progress_status:
        progress_status.score = score
        progress_status.pogress_status = approve
        db.session.commit()

    return {"score": f"{score}",
            "approve": approve
            }, 201


def get_exam_candidate(request):
    assementId = request.view_args.get('assementId', -1)
    info_cv_candidate = Assement.query.filter(Assement.id == assementId).first()
    id_test = info_cv_candidate.test_id
    dict_assement = {
        1: tecnical_test,
        2: logic_test
    }
    assement = []
    for exam in dict_assement[int(id_test)]:
        exam_front = exam.copy()
        exam_front.pop("answer")
        assement.append(exam_front)
    return assement, 200


#@jwt_required
def get_candidate_assements(request):
    try:
        candidateId = int(request.view_args.get('id_candidate', -1))
    except:
        return {"message": "Company Id missing"}, 400
    # candidate_assements = Assement.query.filter(Assement.company_id == candidateId).all()
    try:
        candidate_assements = Assement.query.filter(Assement.candidate_id == candidateId).all()
    except Exception as e:
        return {"message": f"Internal server error {e}"}, 500

    companyInterviewsList =[{
                            "id": inter.id,
                            'candidate_id': inter.candidate_id,
                            'candidate_name': inter.candidate_name,
                            'project_id': inter.project_id,
                            'project_name': inter.project_name,
                            'company_id': inter.company_id,
                            'company_name': inter.company_name,
                            'score': inter.score,
                            'status': inter.status,
                            'typeTest': "Technical Test"
                             } for inter in candidate_assements]

    return companyInterviewsList, 200
