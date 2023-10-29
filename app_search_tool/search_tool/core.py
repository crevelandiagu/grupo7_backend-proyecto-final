import os
import psycopg2


url_posgres = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/')


def get_dandidate(request):

    skill = request.args.get('skill')
    year_exp = False


    if skill:
        return get_candidate_skill(skill)
    elif year_exp:
        pass
    elif skill and year_exp:
        pass
    else:
        pass


def conection_posgres():
    try:

        conn = psycopg2.connect(database="candidate_db",
                                host=url_posgres.split(':')[2].split('@')[1],
                                user=url_posgres.split(':')[1].replace('/', ''),
                                password=url_posgres.split(':')[2].split('@')[0],
                                port="5432")
        cursor = conn.cursor()


        return (True, cursor)
    except Exception as e:
        return (False, {'message': e})


def run_query(query_user):
    conection = conection_posgres()
    if conection[0]:
        cursor = conection[1]

        postgreSQL_select_Query = query_user
        cursor.execute(postgreSQL_select_Query)

        cv_skill_records = cursor.fetchall()
        return cv_skill_records
    return conection_posgres()[1]



def get_candidate_skill(skill):
    skills = set(skill.split('-'))
    my_query = "select * from cv_skills"
    cv_skill_records = run_query(my_query)

    if not isinstance(cv_skill_records, dict):
        len_search = len(skills)
        list_candidate = []
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