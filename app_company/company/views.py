from flask import Blueprint
from flask import request

from .core import (creacion_usuario,
                   autenticar_usuario,
                   self_information)


company = Blueprint('company', __name__)



@company.route("/company/singup", methods=['POST'])
def register_users():
    response, status = creacion_usuario(request)
    return response, status


@company.route("/company/login", methods=['POST'])
def information_user():
    response, status = autenticar_usuario(request)
    return response, status


@company.route("/company/profile", methods=['POST', 'GET'])
def token_user():
    if request.method == 'GET':
        response, status = {}, 200
    elif request.method == 'POST':
        response, status = {}, 200
    else:
        response, status = {"error":""}, 400
    return response, status


@company.route('/company/ping', methods=['GET'])
def root():
    return 'pong'