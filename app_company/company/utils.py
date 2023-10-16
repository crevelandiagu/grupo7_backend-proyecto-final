import re

def is_valid_email(email):
    regular_expression_email = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
    regex = re.compile(regular_expression_email)
    if re.fullmatch(regex, email):
        return True
    return False


def is_validate_password(password):

    regular_expression_password = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    pattern = re.compile(regular_expression_password)
    if re.search(pattern, password):
        return True
    return False