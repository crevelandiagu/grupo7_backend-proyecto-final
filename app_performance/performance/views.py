from sqlalchemy import and_
from flask import Blueprint
from flask import request
import os


from .core import *
from .models import Oferta, db, OfertaSchema

ofertas = Blueprint('payments', __name__)
oferta_schema = OfertaSchema()
users_ip = os.getenv('USERS_URL', "http://127.0.0.1:3000")
user_port = os.getenv('USER_PORT', "3000")
user_endpoint = os.getenv('USER_ENDPOINT', "/app_company/me")

@ofertas.route('/offers/ping', methods=['GET'] )
def root():
    return 'pong'

@ofertas.route('/offers', methods = ['POST'])
def create_offer():
    headers = request.headers
    response_header, status_header = get_token(headers,users_ip, user_port, user_endpoint)
    
    if(status_header == 401):
        return make_response("Invalid token", 401)

    response_body, status_body = validate_create_offer_json(request)
    if(status_body!=200):
        return response_body, status_body

    request_values = {'postId': request.json['postId'],
                          'description': request.json['description'],
                          'size': request.json['size'],
                          'fragile': request.json['fragile'],
                          'offer': request.json['offer']}

    nueva_oferta = Oferta(postId=request_values['postId'], userId=response_header['user_id'], description=request_values['description'], size=request_values['size'], fragile = request_values['fragile'], offer=request_values['offer'])

    db.session.add(nueva_oferta)
    db.session.commit()

    return make_response(oferta_schema.dump(nueva_oferta), 201)

@ofertas.route('/offers', methods = ['GET'])
def get_offers():
    
    #Validate token
    headers=request.headers   
    response_header, status_header = get_token(headers,users_ip, user_port, user_endpoint)
    
    if(status_header == 401):
        return make_response("Invalid token", 401)
    
    #Validate arguments
    post_id=request.args.get('post')
    filter_user=request.args.get('filter')

    if (post_id is not None):
        try:
            post_id=int(post_id)
        except Exception as e:
            return make_response("Bad args", 400)
        if (post_id <= 0):
            return make_response("Bad args", 400)
    
    if (filter_user is not None):
        if (filter_user != "me"):
            return make_response("Bad args", 400)
    
    if (post_id is None and filter_user is None):
        return make_response([oferta_schema.dump(of) for of in Oferta.query.all()], 200)
    if (post_id is None and filter_user is not None):
        return make_response([oferta_schema.dump(of) for of in Oferta.query.filter_by(userId=response_header['user_id'])], 200)
    if (post_id is not None and filter_user is None):
        return make_response([oferta_schema.dump(of) for of in Oferta.query.filter_by(postId=post_id)], 200)
    else:
        return make_response([oferta_schema.dump(of) for of in Oferta.query.filter(and_(Oferta.postId==post_id, Oferta.userId==response_header['user_id']))], 200)

@ofertas.route('/offers/<id_oferta>/', methods=["GET", 'DELETE'])
def single_offer(id_oferta):
    
    #Validate token
    headers=request.headers   
    response_header, status_header = get_token(headers,users_ip, user_port, user_endpoint)
    
    if(status_header == 401):
        return make_response("Invalid token", 401)
    #Validate id
    try:
            id_oferta=int(id_oferta)
    except Exception as e:
        return make_response("Bad args", 400)
    
    if request.method == 'GET':       
        return oferta_schema.dump(Oferta.query.get_or_404(id_oferta))
    elif request.method == 'DELETE':
        oferta = Oferta.query.get_or_404(int(id_oferta))
        db.session.delete(oferta)
        db.session.commit()
        return make_response('Deleted', 204)
