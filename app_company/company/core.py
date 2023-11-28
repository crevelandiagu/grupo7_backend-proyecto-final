import secrets
import hashlib
import random
from datetime import timedelta, datetime
from .models import Companies, db
from .utils import is_validate_password, is_valid_email
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required


def creacion_usuario(request):
    try:
        if not is_validate_password(request.json['password']) and not is_valid_email(request.json["email"]):
            return {"message": "email or password is not validate"}, 412

        existe_email = Companies.query.filter(Companies.email == request.json["email"]).first()
        if existe_email is not None:
            return {"message": "Account already exists. Try with a different one"}, 412

        salt = secrets.token_hex(8)
        password = f"{request.json['password']}{salt}"

        nuevo_usuario = Companies(
            email=request.json["email"],
            password=hashlib.sha256(password.encode()).hexdigest(),
            salt=salt,
            name=request.json["name"],
            nit=random.randint(100000000, 900000000),
            number_employees=random.randint(50, 1000),
            core=['fintech', 'e-commerce', 'bank', 'browser'][random.randint(0, 3)],
            senority=random.randint(3, 50)
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        return {"message": "User successfully added",
                "id": nuevo_usuario.id,
                "name": nuevo_usuario.name,
                "email": nuevo_usuario.email,
                "createdAt": datetime.now().isoformat()
                }, 200
    except Exception as e:
        print(e)
        return {"message": f"Missing: {e}"}, 400


def autenticar_usuario(request):
    try:

        usuario_auth = Companies.query.filter(Companies.email == request.json["email"]).first()

        if usuario_auth is None:
            return {"mensaje": "Usuario con username no exista o contrasena incorrecta"}, 404

        password_input = f"{request.json['password']}{usuario_auth.salt}"
        password = Companies.query.filter(Companies.email == request.json["email"],
                                         Companies.password == hashlib.sha256(password_input.encode()).hexdigest()
                                         ).first()

        if password is None:
            return {"mensaje": "Usuario con username no exista o contrasena incorrecta"}, 404

        token_user = create_access_token(identity=usuario_auth.id)
        db.session.commit()
        return {"mensaje": "Inicio de sesión exitoso",
                "id": usuario_auth.id,
                "token": token_user,
                "name": usuario_auth.name,
                }, 200

    except Exception as e:
        print(e)
        return {"mensaje": f"falta {e}"}, 400


# @jwt_required()
def build_basicinfo(request):
    id_company = request.view_args.get('id_company', -1)
    info_company = Companies.query.filter(Companies.id == id_company).first()

    if request.method == 'GET':

        basic_info = {
            'name': info_company.name,
            'nit': info_company.nit,
            'email': info_company.email,
            'number_employees': info_company.number_employees,
            'core': info_company.core,
            'senority': info_company.senority,
        }

        return basic_info, 200

    elif request.method == 'POST':
        info_company.nit = random.randint(100000000, 900000000)
        info_company.number_employees = random.randint(50, 1000)
        info_company.core = ['fintech', 'e-commerce', 'bank', 'browser'][random.randint(0, 3)]
        info_company.senority = random.randint(3, 50)
        db.session.commit()
        return {"message": "Company add info basic successfully"}, 200
    return {"message": "No exist "}, 400



