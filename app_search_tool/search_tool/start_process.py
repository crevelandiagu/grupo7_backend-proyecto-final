import os
import logging
import requests
from .utils_gcp.gcp_pub_sub import GCP
from .search_cv import request_app

def get_info_candidate(candidateId):
    id_candidate = candidateId

    CANDIDATE_URI = os.getenv('CANDIDATE_URL', "http://127.0.0.1:3000/")
    candidate_path_basicinfo = "candidate/profile/basicinfo/"

    url_basicinfo = f"{CANDIDATE_URI}{candidate_path_basicinfo}{id_candidate}"


    basicinfo, code_basicinfo = request_app(url_basicinfo)

    info_cv = {}
    if basicinfo and code_basicinfo == 200:
        info_cv['basicinfo'] = basicinfo

    if len(info_cv) == 0:
        return info_cv, 401
    return info_cv, 200

def post_candidate_chose_one(candidateId):

    id_candidate = candidateId

    CANDIDATE_URI = os.getenv('CANDIDATE_URL', "http://127.0.0.1:3000/")
    candidate_path_basicinfo = "candidate/process/"

    url_basicinfo = f"{CANDIDATE_URI}{candidate_path_basicinfo}{id_candidate}"

    try:
        response_token = requests.post(url=url_basicinfo, json={"chooseOne": True})
    except Exception as e:
        return e, 401


def chosen_one_candidate(request):

    message_start_process = {
        "where": "candidate-chosen-one",
        "candidateId": request.json['candidateId'],
        "projectId": request.json['projectId'],
        "companyId": request.json['companyId'],
    }
    info_candidate, status = get_info_candidate(request.json['candidateId'])
    post_candidate_chose_one(request.json['candidateId'])
    if status == 200:
        message_start_process.update(info_candidate)
    logging.warning(f'Watch!')
    try:
        logging.warning(f'Watch! send')
        publicar = GCP()
        publicar.publisher_message(message_start_process)
    except Exception as e:
        logging.warning(f'Watch! NO SEND {e}')
        print({"message": f"{e}"})
    return {"message": "Candidate has started the process"}, 200

