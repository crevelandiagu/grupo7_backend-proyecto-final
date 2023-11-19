import secrets
import hashlib
from .models import Assement, db
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from datetime import datetime
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

    return {}, 200


#@jwt_required
def candidate_assements(request):

    return {}, 200


#@jwt_required
def evaluate_company_interview(request):

    return {"message": f""}, 200