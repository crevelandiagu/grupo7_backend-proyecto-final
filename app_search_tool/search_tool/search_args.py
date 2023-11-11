from .connection_db import ConnectionDB

def get_dandidate(query):

    skill = query.skill
    year_exp = query.experienceYears

    if skill and year_exp:
        return get_candidate_general(skill=skill, year_exp=year_exp)
    elif year_exp:
        return get_candidate_general(year_exp=year_exp)
    elif skill:
        return get_candidate_general(skill=skill)
    else:
        return get_candidate_general()


def get_candidate_general(skill=[], year_exp=0):
    conn_db = ConnectionDB()

    if year_exp and skill or year_exp:
        my_query = f"select * from cv_skills where years_exp >= {year_exp}"
    else:
        my_query = "select * from cv_skills"

    skills = set(skill.split('-')) if skill else set()
    cv_skill_records = conn_db.run_query(my_query)

    if not isinstance(cv_skill_records, dict):
        len_search = len(skills) if skill else -1
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