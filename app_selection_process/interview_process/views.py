from flask import Blueprint
from flask import request
from flask import session
from flask import Response
from flask import url_for, flash
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

from .core import (creacion_publicacion,
                   creacion_oferta_publicacion,
                   consultar_publicacion)


publico = Blueprint('interview_process', __name__)


@publico.route("/public/posts", methods=['POST'])
def register_public_post():
    response, status = creacion_publicacion(request)
    return response, status


@publico.route("/public/posts/<id>/offers", methods=['POST'])
def register_public_ofert(id):
    response, status = creacion_oferta_publicacion(request, id)
    return response, status


@publico.route("/public/posts/<int:id>/", methods=['GET'])
def information_user(id):
    response, status = consultar_publicacion(request, id)
    return response, status


@publico.route('/public/ping', methods=['GET'] )
def root():
    return 'pong'

