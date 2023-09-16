import requests
from flask import make_response

def get_token(headers, users_ip, user_port, user_endpoint):
    try:
        token=headers.get('Authorization').split(" ")[1]
    except Exception as e:
        return "Invalid token", 401        
    response_token= requests.get(f'{users_ip}{user_endpoint}', headers={"Authorization": f'Bearer {token}'})
    
    if (response_token.status_code == 401):
        return "Invalid token", 401
    return {"user_id":response_token.json()['id']}, 200

def validate_create_offer_json(request):
    
    #Validate all fields are in the json
    try:
        request_values = {'postId': request.json['postId'],
                          'description': request.json['description'], 
                          'size': request.json['size'],
                          'fragile': request.json['fragile'],
                          'offer': request.json['offer']}
    except Exception as e:
        print(e)
        return {"mensaje": f"falta {e}"}, 400
    
    #Validate values
    if ((type(request_values['postId']) is not int)):
        return {"msg":"PostId must be a number"}, 412    
    if (type(request_values['fragile']) is not bool):
        return {"msg":"fragile must be True or False"}, 412
    if (request_values['size'] not in ['SMALL','MEDIUM','LARGE']):
        return {"msg":"size must be SMALL, MEDIUM or LARGE"}, 412
    if ((type(request_values['offer']) is not int) and (type(request_values['offer']) is not float)):
        return {"msg":"Offer must be a number greater than 0"}, 412
    
    if (len(request_values['description'])>=141):
        return {"msg":"description must have less than 141 characters"}, 412
    
    if (request_values['postId'] <=0 or request_values['offer'] <=0):
        return {"msg":"ids and offer must be greater than 0"}, 412

    return "ok", 200
