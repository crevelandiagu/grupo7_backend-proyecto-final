import secrets
import hashlib
from datetime import timedelta, datetime
from .models import Candidates, db
from .utils import validate_cv_fields
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required


def creacion_usuario(request):
    try:

        existe_email = Candidates.query.filter(Candidates.email == request.json["email"]).first()
        if existe_email is not None:
            return {"mensaje": "El correo ya existe, pruebe con otro"}, 412

        salt = secrets.token_hex(8)
        password = f"{request.json['password']}{salt}"

        nuevo_usuario = Candidates(
            name=request.json["name"],
            lastname=request.json['lastname'],
            email=request.json["email"],
            password=hashlib.sha256(password.encode()).hexdigest(),
            salt=salt,
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        return {"mensaje": "usuario creado exitosamente",
                "id": nuevo_usuario.id,
                "name": nuevo_usuario.name,
                "lastname": nuevo_usuario.lastname,
                "email": nuevo_usuario.email,
                "createdAt": datetime.now().isoformat()
                }, 201
    except Exception as e:
        print(e)
        return {"mensaje": f"falta {e}"}, 400


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


@jwt_required
def create_user_cv(request):
    
    try:
        status, cv_values = validate_cv_fields(request)
        return
    except Exception as e:
        print(e)
        return {"message": f"falta {e}"}, 400
