import requests
from flask import jsonify
from datetime import datetime, timedelta
from .models import db, Publicacion, PublicacionSchema

publicacion_schema = PublicacionSchema

def get_token(headers, users_ip, user_port, user_endpoint):
    try:
        token = headers.get('Authorization').split(" ")[1]
    except Exception as e:
        return "Invalid token", 401
    response_token = requests.get(f'{users_ip}{user_endpoint}', headers={
                                  "Authorization": f'Bearer {token}'})

    if (response_token.status_code == 401):
        return "Invalid token", 401

    return {"user_id":response_token.json()['id']}, 200

def create_post_(request, user):
  try:
    new_post = Publicacion(
      routeId=request.json["routeId"],
      userId=user.get('user_id'),
      plannedStartDate=datetime.strptime(request.json["plannedStartDate"], '%Y-%m-%d'),
      plannedEndDate=datetime.strptime(request.json["plannedEndDate"], '%Y-%m-%d')
    )
    if new_post.plannedStartDate <= datetime.today() or new_post.plannedStartDate > (datetime.today() + timedelta(days=30)):
      return {"mensaje": "Fecha inicio debe ser mayor y maximo 30 días posterior a fecha actual"}, 412  
    if new_post.plannedStartDate >= new_post.plannedEndDate:
      return {"mensaje": "Fecha final debe ser mayor a fecha inicial"}, 412  
    db.session.add(new_post)
    db.session.commit()
    return {"id": new_post.id, "userId": new_post.userId, "createdAt": new_post.createdAt.strftime('%Y-%m-%d, %H:%M.%S')}, 201
  except Exception as e:
        return {"mensaje": f"Campo {e} es requerido"}, 400

def search_post_(request, user):
  user_id = user.get('user_id')
  start_date = request.args.get("when")
  route_id = request.args.get("route")
  user_me = request.args.get("filter")

  if start_date is not None:
    try:
      start_date = datetime.strptime(start_date, '%Y-%m-%d')
    except Exception as e:
      return {"mensaje": f"Parametro start_date no tiene el formato correcto"}, 400

  if route_id is not None:
    try:
      route_id = int(route_id)
    except Exception as e:
      print(e)
      return {"mensaje": f"Parametro route_id no tiene el formato correcto"}, 400

  if user_me is not None and user_me != "me":
      return {"mensaje": f"Parametro filter no tiene el formato correcto"}, 400
  
  if start_date and route_id and user_me:
    post_all_filter = Publicacion.query.filter(Publicacion.userId == user_id, Publicacion.plannedStartDate == start_date, Publicacion.routeId == route_id, ).all()
    publicacion_schema = PublicacionSchema(many=True)
    return jsonify(publicacion_schema.dump(post_all_filter)), 200
  
  if start_date and route_id:
    post_date_route = Publicacion.query.filter(Publicacion.plannedStartDate == start_date, Publicacion.routeId == route_id, ).all()
    publicacion_schema = PublicacionSchema(many=True)
    return jsonify(publicacion_schema.dump(post_date_route)), 200

  if start_date and user_me:
    post_date_user = Publicacion.query.filter(Publicacion.userId == user_id, Publicacion.plannedStartDate == start_date).all()
    publicacion_schema = PublicacionSchema(many=True)
    return jsonify(publicacion_schema.dump(post_date_user)), 200

  if start_date:
    post_date = Publicacion.query.filter(Publicacion.plannedStartDate == start_date).all()
    publicacion_schema = PublicacionSchema(many=True)
    return jsonify(publicacion_schema.dump(post_date)), 200

  if route_id:
    post_route = Publicacion.query.filter(Publicacion.routeId == route_id).all()
    publicacion_schema = PublicacionSchema(many=True)
    return jsonify(publicacion_schema.dump(post_route)), 200

  if route_id and user_me:
    post_route_user = Publicacion.query.filter(Publicacion.userId == user_id, Publicacion.routeId == route_id ).all()
    publicacion_schema = PublicacionSchema(many=True)
    return jsonify(publicacion_schema.dump(post_route_user)), 200
  
  if user_me:
    post_user = Publicacion.query.filter(Publicacion.userId == user_id).all()
    publicacion_schema = PublicacionSchema(many=True)
    return jsonify(publicacion_schema.dump(post_user)), 200

  if not start_date and not route_id and not user_me:
    post_all = Publicacion.query.all()
    publicacion_schema = PublicacionSchema(many=True)
    return jsonify(publicacion_schema.dump(post_all)), 200

def get_post_(id_post, response_header):
  try:
    post_id = Publicacion.query.filter(Publicacion.id == id_post).one()
  except Exception as e:
    return {"mensaje": f"No existe la publicación"}, 404 

 # if post_id.userId != response_header['user_id']:
  #  return {"mensaje": f"Usuario no autorizado"}, 403

  publicacion_schema = PublicacionSchema()
  return jsonify(publicacion_schema.dump(post_id)), 200 

