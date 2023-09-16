import secrets
import hashlib
from datetime import timedelta, datetime
from .models import Companies, db
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required


def creacion_usuario(request):
    try:
        existe_usuario = Companies.query.filter(Companies.username == request.json["username"]).first()
        existe_email = Companies.query.filter(Companies.email == request.json["email"]).first()
        if existe_usuario is not None or existe_email is not None:
            return {"mensaje": "El usuario ya existe, pruebe con otro"}, 412

        salt = secrets.token_hex(8)
        password = f"{request.json['password']}{salt}"

        nuevo_usuario = Companies(
            username=request.json["username"],
            email=request.json["email"],
            password=hashlib.sha256(password.encode()).hexdigest(),
            salt=salt,
        )
        db.session.add(nuevo_usuario)
        db.session.commit()
        return {"mensaje": "usuario creado exitosamente",
                "id": nuevo_usuario.id,
                "createdAt": datetime.now().isoformat()
                }, 201
    except Exception as e:
        print(e)
        return {"mensaje": f"falta {e}"}, 400


def autenticar_usuario(request):
    try:

        usuario_auth = Companies.query.filter(Companies.username == request.json["username"]).first()

        if usuario_auth is None:
            return {"mensaje": "Usuario con username no exista o contrasena incorrecta"}, 404

        password_input = f"{request.json['password']}{usuario_auth.salt}"
        password = Companies.query.filter(Companies.username == request.json["username"],
                                         Companies.password == hashlib.sha256(password_input.encode()).hexdigest()
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

    return {"id": 'id',
            "username": 'username',
            "email": 'email'}, 200


