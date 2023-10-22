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


