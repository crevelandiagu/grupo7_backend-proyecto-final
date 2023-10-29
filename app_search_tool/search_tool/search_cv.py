import os
import requests

def request_app(url):

    try:
        response_token = requests.get(url=url)
    except Exception as e:
        return e, 401

    return response_token.json(), 200

def get_cv_candidate(request):
    id_candidate = request.view_args.get('id_candidate', -1)

    CANDIDATE_URI = os.getenv('CANDIDATE_URL', "http://127.0.0.1:3000")
    candidate_path_basicinfo = "/candidate/profile/basicinfo/"
    candidate_path_experience = "/candidate/profile/experience/"
    candidate_path_education = "/candidate/profile/education/"
    candidate_path_certificates = "/candidate/profile/certificates/"

    url_basicinfo = f"{CANDIDATE_URI}{candidate_path_basicinfo}{id_candidate}"
    url_experience = f"{CANDIDATE_URI}{candidate_path_experience}{id_candidate}"
    url_education = f"{CANDIDATE_URI}{candidate_path_education}{id_candidate}"
    url_certificates = f"{CANDIDATE_URI}{candidate_path_certificates}{id_candidate}"

    basicinfo, code_basicinfo = request_app(url_basicinfo)
    experience, code_experience = request_app(url_experience)
    education, code_education = request_app(url_education)
    certificates, code_certificates = request_app(url_certificates)

    info_cv = {}
    if basicinfo and code_basicinfo == 200:
        info_cv['basicinfo'] = basicinfo

    if experience and code_experience == 200:
        info_cv.update(experience)

    if education and code_education == 200:
        info_cv.update(education)

    if certificates and code_certificates == 200:
        info_cv.update(certificates)

    if len(info_cv)==0:
        return info_cv, 401
    return info_cv, 200
