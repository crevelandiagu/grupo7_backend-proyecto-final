from .models import CurriculumVitae, db
from email_validator import validate_email, EmailNotValidError
from password_strength import PasswordPolicy

def validate_email_address(email):
    
    try:
        email_validated=validate_email(email)
        return True, "Valid email"
    except EmailNotValidError as e:
        print(str(e))
        return False, str(e)

def validate_password(password):

    policy = PasswordPolicy.from_names(
        length=8,
        uppercase=1,
        numbers=1,
        special=1,
        nonletters=2
    )
    if(len(policy.test(password)) != 0):
        return False
    return True


def validate_cv_fields(request):

    data_cv = dict(request.json)
    name = data_cv.get('basicInfo', {}).get('name', "")
    lastname = data_cv.get('basicInfo', {}).get('lastname', "")
    birthday = data_cv.get('basicInfo', {}).get('birthday', "")
    nacionality = data_cv.get('basicInfo', {}).get('nacionality', "")

    experience = str(data_cv.get('experience', []))
    education = str(data_cv.get('education', []))
    skills = str(data_cv.get('skills', []))
    certificates = str(data_cv.get('certificates', []))

    new_cv = CurriculumVitae(
            skills = skills,            
            work_experience = experience,
            education = education,
            certificates = certificates
        )
    db.session.add(new_cv)
    db.session.commit()
    
    return 0
'''
{
    "basicinfo":
    {
        "name":"ccc",
        "lastname":"",
        "birthday":"",
        "nacionality":""
    },
    "experience":[
        {
        },
        {
            "a":"",
            "skills": [
            ]
        }
    ],
    "education":[
        {
            "a":"",
            "skills": [
            ]
        },
        {
        }
    ],
    "skills":[
        {
        },
        {
        }
    ],
    "certificates":[
        {
            "a":"",
        },
        {
        }
    ]
}
'''