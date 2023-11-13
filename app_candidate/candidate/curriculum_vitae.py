from flask import jsonify
from datetime import datetime, timedelta
from .models import (
    db,
    Candidates,
    CvExperience,
    CvEducation,
    CvCertificates,
    CvSkills
                     )


def build_basicinfo(request):
    id_candidate = request.view_args.get('id_candidate', -1)
    info_candidate = Candidates.query.filter(Candidates.id == id_candidate).first()

    if request.method == 'GET':

        basic_info = {
            'nacionality': info_candidate.nacionality,
            'phone_number': info_candidate.phone_number,
            'email': info_candidate.email
        }

        if info_candidate.name:
            basic_info['name'] = info_candidate.name
        if info_candidate.lastname:
            basic_info['lastname'] = info_candidate.lastname

        name = basic_info.get('name', 'No')
        lastname = basic_info.get('lastname', 'Name')

        basic_info['initial_latter'] = f'{name.split(" ")[0][0].upper()}' \
                                       f'{lastname.split(" ")[0][0].upper()}'

        basic_info['name'] = info_candidate.name
        basic_info['lastname'] = info_candidate.lastname
        basic_info['full_name'] = f'{name} {lastname}'

        return basic_info, 200

    elif request.method == 'POST':
        build_skill_candidate(request)
        info_candidate.name = request.json.get('name', 'None')
        info_candidate.lastname = request.json.get('lastname', 'None')
        info_candidate.birthdate = request.json.get('birthdate', 'None')
        info_candidate.nacionality = request.json.get('nacionality')
        info_candidate.phone_number = request.json.get('phone_number')
        info_candidate.number_id = request.json.get('number_id')
        db.session.commit()
        return {"message": "User add info basic successfully"}, 200
    return {"message": "No exist "}, 400

def build_experience(request):

    id_candidate = request.view_args.get('id_candidate', -1)
    data_experience = CvExperience.query.filter(CvExperience.candidate_id == id_candidate).all()

    if request.method == 'GET':

        list_experience = [experience.experience for experience in data_experience]
        return {'experience': list_experience}, 200

    elif request.method == 'POST':
        build_skill_candidate(request)

        experience = {
            "position": request.json.get('position'),
            "company_name": request.json.get('company_name'),
            "start_date": request.json.get('start_date'),
            "end_date": request.json.get('end_date'),
            "place": request.json.get('place'),
            "skills": request.json.get('skills')
        }
        new_experience = CvExperience(
            experience=experience,
            candidate_id=id_candidate,
        )
        db.session.add(new_experience)
        db.session.commit()
        return {"message": "User add experience successfully"}, 200
    return {"message": "No exist "}, 400


def build_education(request):

    id_candidate = request.view_args.get('id_candidate', -1)
    data_education = CvEducation.query.filter(CvEducation.candidate_id == id_candidate).all()

    if request.method == 'GET':
        list_educatio = [education.education for education in data_education]
        return {'education': list_educatio}, 200
    elif request.method == 'POST':
        education = {
            "university": request.json.get('university'),
            "subject": request.json.get('subject'),
            "start_date": request.json.get('start_date'),
            "end_date": request.json.get('end_date'),
            "skills": request.json.get('skills')
        }
        new_education = CvEducation(
            education=education,
            candidate_id=id_candidate,
        )
        db.session.add(new_education)
        db.session.commit()
        return {"message": "User add education successfully"}, 200
    return {"message": "No exist "}, 400


def build_certificates(request):

    id_candidate = request.view_args.get('id_candidate', -1)
    data_certificates = CvCertificates.query.filter(CvCertificates.candidate_id == id_candidate).all()

    if request.method == 'GET':
        list_educatio = [certificates.certificates for certificates in data_certificates]
        return {'certificates': list_educatio}, 200
    elif request.method == 'POST':
        certificates = {
            "name_certificate": request.json.get('name_certificate'),
            "company": request.json.get('company'),
            "expedition_date": request.json.get('start_date'),
            "date_expiry": request.json.get('end_date'),
        }
        new_certificates = CvCertificates(
            certificates=certificates,
            candidate_id=id_candidate,
        )
        db.session.add(new_certificates)
        db.session.commit()
        return {"message": "User add certificates successfully"}, 200
    return {"message": "No exist "}, 400


def build_skill_candidate(request):
    id_candidate = request.view_args.get('id_candidate', -1)
    info_cv_candidate = CvSkills.query.filter(CvSkills.candidate_id == id_candidate).first()

    skills_candidate = []
    if request.json.get('skills'):
        skills_candidate = request.json.get('skills')

    years_exp = 0
    if request.json.get('start_date') and request.json.get('end_date'):
        years_exp = subtract_date(request.json.get('start_date'), request.json.get('end_date'))

    if not info_cv_candidate:
        name = request.json.get('name', 'No Name')
        lastname = request.json.get('lastname', 'No LastName')
        new_experience = CvSkills(
            name=name,
            lastname=lastname,
            skills={"skills": skills_candidate},
            years_exp=years_exp,
            candidate_id=id_candidate,
        )
        db.session.add(new_experience)
        db.session.commit()
        return 0

    if info_cv_candidate.skills.get('skills'):
        skills_candidate = list(set(info_cv_candidate.skills.get('skills') + skills_candidate))

    info_cv_candidate.skills = {"skills": skills_candidate}
    info_cv_candidate.years_exp = float(years_exp) + float(info_cv_candidate.years_exp)
    db.session.commit()
    return 0


def subtract_date(fecha_cad1='2020-11-08', fecha_cad2='2023-11-08'):

    fecha_cad1 = fecha_cad1
    fecha_cad2 = fecha_cad2
    fecha1 = datetime.strptime(fecha_cad1, '%Y-%m-%d')
    fecha2 = datetime.strptime(fecha_cad2, '%Y-%m-%d')

    dias = round((fecha2 - fecha1) / timedelta(days=365), 2)
    return dias