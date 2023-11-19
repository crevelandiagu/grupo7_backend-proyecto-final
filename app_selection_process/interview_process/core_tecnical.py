# from .models import Assement, AssementSchema
# from app_selection_process.interview_process.models import Assement, db
from .models import Assement
from .exam import tecnical_test, logic_test


#@jwt_required
def take_exam_candidate(request):
    # [{id: 1, answer: "2"}]
    dict_assement = {
        1: tecnical_test,
        2: logic_test
    }
    assement = dict_assement[request.view_args.get('id_test', 1)]
    score = 0
    for answer in request.json:
        id = answer.get('id')
        result = assement[id]
        if answer.get('answer') == result.get('answer'):
            score += 1

    return {"score": f"{score}",
            "approve": True if score > 3 else False
            }, 201


#@jwt_required
def get_candidate_assements(request):
    try:
        candidateId = int(request.view_args.get('id_candidate', -1))
    except:
        return {"message": "Company Id missing"}, 400
    # candidate_assements = Assement.query.filter(Assement.company_id == candidateId).all()
    try:
        candidate_assements = Assement.query.filter(Assement.company_id == candidateId).all()
    except Exception as e:
        return {"message": f"Internal server error {e}"}, 500

    companyInterviewsList =[]#= [AssementSchema.dump(inter) for inter in candidate_assements]

    return companyInterviewsList, 200



#@jwt_required
def candidate_assements(request):

    return {}, 200


#@jwt_required
def evaluate_company_interview(request):

    return {"message": f""}, 200