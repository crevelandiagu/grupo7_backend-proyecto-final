from .connection_db import ConnectionDB

def get_dandidate(request):

    skill = request.args.get('skill')
    year_exp = request.args.get('experienceYears')

    if skill and year_exp:
        return get_candidate_skill_year_exp(skill, year_exp)
    elif year_exp:
        return get_candidate_year_exp(year_exp)
    elif skill:
        return get_candidate_skill(skill)
    else:
        pass



def get_candidate_skill(skill):
    conn_db = ConnectionDB()
    skills = set(skill.split('-'))
    my_query = "select * from cv_skills"
    cv_skill_records = conn_db.run_query(my_query)

    if not isinstance(cv_skill_records, dict):
        len_search = len(skills)
        list_candidate = []
        if cv_skill_records:
            for candidate in cv_skill_records:
                if len(skills & set(candidate[1].get('skills'))) >= len_search:
                    list_candidate.append({
                        "name":candidate[3],
                        "lastName": candidate[4],
                        "skills": candidate[1],
                        "years_exp": candidate[2],
                        "candidateId": candidate[-1],
                    })
        return list_candidate, 200
    return cv_skill_records, 400

def get_candidate_year_exp(year_exp):
    conn_db = ConnectionDB()
    year_exp = float(year_exp)
    my_query = f"select * from cv_skills where years_exp >= {year_exp}"
    cv_skill_records = conn_db.run_query(my_query)

    if not isinstance(cv_skill_records, dict):
        list_candidate = []
        if cv_skill_records:
            for candidate in cv_skill_records:
                list_candidate.append({
                    "name":candidate[3],
                    "lastName": candidate[4],
                    "skills": candidate[1],
                    "years_exp": candidate[2],
                    "candidateId": candidate[-1],
                })
        return list_candidate, 200
    return cv_skill_records, 400


def get_candidate_skill_year_exp(skill, year_exp):
    conn_db = ConnectionDB()
    year_exp = float(year_exp)
    skills = set(skill.split('-'))
    my_query = f"select * from cv_skills where years_exp >= {year_exp}"
    cv_skill_records = conn_db.run_query(my_query)

    if not isinstance(cv_skill_records, dict):
        len_search = len(skills)
        list_candidate = []
        if cv_skill_records:
            for candidate in cv_skill_records:
                if len(skills & set(candidate[1].get('skills'))) >= len_search:
                    list_candidate.append({
                        "name":candidate[3],
                        "lastName": candidate[4],
                        "skills": candidate[1],
                        "years_exp": candidate[2],
                        "candidateId": candidate[-1],
                    })
        return list_candidate, 200
    return cv_skill_records, 400

'''
f"select name.candidatte from candidatte where id.candidatte in {id_candidate}"
'''