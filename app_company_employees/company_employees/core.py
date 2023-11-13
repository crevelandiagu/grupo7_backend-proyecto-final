import requests
import re
import secrets
import hashlib
from datetime import datetime, timedelta
from .models import db,EmployeeCompany


def creacion_usuario(request):
  try:
    if not is_validate_password(request.json['password']) and not is_valid_email(request.json["email"]):
      return {"message": "email or password is not validate"}, 412

    existe_email = EmployeeCompany.query.filter(EmployeeCompany.email == request.json["email"]).first()
    if existe_email is not None:
      return {"message": "Account already exists. Try with a different one"}, 412

    salt = secrets.token_hex(8)
    password = f"{request.json['password']}{salt}"

    nuevo_usuario = EmployeeCompany(
      email=request.json["email"],
      password=hashlib.sha256(password.encode()).hexdigest(),
      salt=salt,
      company_id=request.json["companyId"]
    )
    db.session.add(nuevo_usuario)
    db.session.commit()
    return {"message": "User successfully added",
            "id": nuevo_usuario.id,
            "email": nuevo_usuario.email,
            "createdAt": datetime.now().isoformat()
            }, 200
  except Exception as e:
    print(e)
    return {"message": f"Missing: {e}"}, 400


def get_employees(request):
    id_company = request.view_args.get('id_company', -1)
    info_company_employees = EmployeeCompany.query.filter(EmployeeCompany.company_id == id_company).all()
    list_employee=[]
    for employee in info_company_employees:
        list_employee.append({
            'employeeId': employee.id,
            'email': employee.email,
            'companyId': employee.company_id,
            'companyProjectId': employee.company_project_id
        })
    return list_employee, 200


def is_valid_email(email):
    regular_expression_email = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
    regex = re.compile(regular_expression_email)
    if re.fullmatch(regex, email):
      return True
    return False


def is_validate_password(password):
  regular_expression_password = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
  pattern = re.compile(regular_expression_password)
  if re.search(pattern, password):
    return True
  return False