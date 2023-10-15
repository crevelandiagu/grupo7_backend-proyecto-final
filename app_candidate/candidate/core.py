import secrets
import hashlib
from datetime import timedelta, datetime
from .models import Candidates, db
from .utils import validate_cv_fields, validate_email_address, validate_password
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from email_validator import validate_email, EmailNotValidError
from password_strength import PasswordPolicy


def creacion_usuario(request):
    try:

        valid_email = False
        valid_email, validation_email_mess = validate_email_address(request.json["email"])

        if (not valid_email):
            return {"message": validation_email_mess}, 412

        valid_password = False
        valid_password = validate_password(request.json["password"])

        if (not valid_password):
            return {"message": "Password must have at least: 8 characters, 1 uppercase letter, 1 number and 1 special character"}, 412

        existe_email = Candidates.query.filter(Candidates.email == request.json["email"]).first()
        if existe_email is not None:
            return {"message": "Account already exists. Try with a different one"}, 412

        salt = secrets.token_hex(8)
        password = f"{request.json['password']}{salt}"

        nuevo_usuario = Candidates(
            email=request.json["email"],
            password=hashlib.sha256(password.encode()).hexdigest(),
            salt=salt,
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        return {"message": "User successfully added",
                "id": nuevo_usuario.id,
                "email": nuevo_usuario.email,
                "createdAt": datetime.now().isoformat()
                }, 201
    except Exception as e:
        print(e)
        return {"message": f"Missing: {e}"}, 400


def autenticar_usuario(request):
    try:

        usuario_auth = Candidates.query.filter(Candidates.email == request.json["email"]).first()

        if usuario_auth is None:
            return {"mensaje": "Usuario con username no exista o contrasena incorrecta"}, 404

        password_input = f"{request.json['password']}{usuario_auth.salt}"
        password = Candidates.query.filter(Candidates.email == request.json["email"],
                                         Candidates.password == hashlib.sha256(password_input.encode()).hexdigest()
                                         ).first()

        if password is None:
            return {"mensaje": "Usuario con username no exista o contrasena incorrecta"}, 404

        token_user = create_access_token(identity=usuario_auth.id)
        db.session.commit()
        return {"mensaje": "Inicio de sesión exitoso",
                "id": usuario_auth.id,
                "token": token_user,
                }, 200

    except Exception as e:
        print(e)
        return {"mensaje": f"falta {e}"}, 400


@jwt_required()
def self_information(request):


    return {"id": 0,
            "username": 'username',
            "email": 'email'}, 200


#@jwt_required
def create_user_cv(request):
    
    try:
        status = validate_cv_fields(request)
        return {"message": "CV created"}, 201
    
    except Exception as e:
        print(e)
        return {"message": f"falta {e}"}, 400

