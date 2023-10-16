from flask import Blueprint, request
from flask import jsonify
from .models import db, Trayecto
from .serializer import ResourceSerializer
from .core import *
import os


users_ip = os.getenv('USERS_URL', "http://127.0.0.1:3000")
user_port = os.getenv('USER_PORT',"3000")
user_endpoint = os.getenv('USER_ENDPOINT',"/app_company/me")

trayectos = Blueprint("project", __name__)

@trayectos.route("/routes", methods=["POST"])
def create_route():
      
  #  data = request.get_json(force=True)
    respuesta, status = get_token(request.headers, users_ip=users_ip, 
                                  user_port=user_port, user_endpoint=user_endpoint)
    
    if status == 401:
        return jsonify("token invalido"), 401
    
    
       
    sourceAirportCode = request.json.get("sourceAirportCode")
    sourceCountry = request.json.get("sourceCountry")
    destinyAirportCode = request.json.get("destinyAirportCode")
    destinyCountry = request.json.get("destinyCountry")
    bagCost = request.json.get("bagCost")

    if None in [sourceAirportCode, sourceCountry, destinyAirportCode, destinyCountry, bagCost]:
        return jsonify("Alguno de los campos no esta presente en la solicitud"), 400
    
    #validacion

    if v_code(sourceAirportCode) is None:
        return jsonify(f"El valor enviado sourceAirportCode = {sourceAirportCode} no tiene el formato correcto"), 400
    
    if v_code(destinyAirportCode) is None:
        return jsonify(f"El valor enviado destinyAirportCode = {destinyAirportCode} no tiene el formato correcto"), 400
    
    if va_nombre_pais(destinyCountry) is None:
        return jsonify(f"El valor enviado destinyCountry = {destinyCountry} no tiene el formato correcto"), 400

    if va_nombre_pais(sourceCountry) is None:
        return jsonify(f"El valor enviado sourceCountry = {sourceCountry} no tiene el formato correcto"), 400
    
    try:
        cost = float(bagCost)
        if cost <= 0:
            return jsonify(f"El valor enviado bagCost = {bagCost} tiene que ser un número mayor a cero"), 400
    except Exception as err:
        return jsonify(f"El valor enviado {bagCost} no es un número"), 400

 
    trayecto = Trayecto(sourceAirportCode=sourceAirportCode,
     sourceCountry=sourceCountry, destinyAirportCode=destinyAirportCode,
      destinyCountry=destinyCountry, bagCost=bagCost)

  #  print(trayecto.sourceAirportCode)
    
    if se_puede_agregar_trayecto(trayecto=trayecto, model=Trayecto):
        db.session.add(trayecto)
        db.session.commit()
   # print(trayecto)
        return jsonify([ResourceSerializer.serialize_trayecto_creado(trayecto)]), 201
    
    return jsonify("El trayecto ya existe y se encuentra activo"), 412


@trayectos.route("/routes", methods=["GET"])
def buscar_trayecto():

    respuesta, status = get_token(request.headers, users_ip=users_ip,
                                  user_port=user_port, user_endpoint=user_endpoint)

    if status == 401:
        return jsonify("token invalido"), 401

    params = request.args.to_dict()

    from_ = params.get("from", None)
    to = params.get("to", None)
    when = params.get("when", None)

    try:
        trayectos = query_trayectos(from_=from_, to=to, when=when, model=Trayecto)
    except Exception as err:
        return jsonify(str(err)), 400
        
    return jsonify([ResourceSerializer.serialize_trayecto_encontrado(trayecto) for trayecto in trayectos]), 200
    

@trayectos.route("/routes/<id>", methods=["GET", 'DELETE'])
def retornar_trayecto_id(id):
    respuesta, status = get_token(request.headers, users_ip=users_ip,
                                  user_port=user_port, user_endpoint=user_endpoint)

    if status == 401:
        return jsonify("token invalido"), 401
    if request.method == 'GET':

        try:
            id = int(id)
        except Exception as e:
            return {"mensaje": f"El id no es un número"}, 400

        # if not isinstance(id_post, int):
        #     return jsonify("El id no es un número"), 400

        trayecto = Trayecto.query.filter_by(id=id).first()

        if not trayecto:
           return jsonify("No existe el trayecto con id: {}".format(id)), 404

        return jsonify([ResourceSerializer.serialize_trayecto_encontrado(trayecto)]), 200
    elif request.method == 'DELETE':
        trayecto = Trayecto.query.get_or_404(int(id))
        db.session.delete(trayecto)
        db.session.commit()
        return {"msj": 'Borrado'}, 204



@trayectos.route("/routes/ping", methods=["GET"])
def health():
    return "pong", 200
