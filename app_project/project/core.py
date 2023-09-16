import requests
import datetime
import re
from sqlalchemy import and_

def get_token(headers, users_ip, user_port, user_endpoint):
  #  print(headers.get('Authorization'))
    try:
        token=headers.get('Authorization').split(" ")[1]
    except Exception as e:
        return "Invalid token", 401        
    response_token= requests.get(f'{users_ip}{user_endpoint}', headers={"Authorization": f'Bearer {token}'})
    
    if (response_token.status_code == 401):
        return "Invalid token", 401

    return {"user_id":response_token.json()['id']}, 200


def query_trayectos(from_, to, when, model):

    filters= []
    

    if from_:
        if v_code(from_):
            filters.append(model.sourceAirportCode.like(from_))
        else:
            raise Exception("El parametro from tiene un formato incorrecto")
           
    if to:
        if v_code(to):
            filters.append(model.destinyAirportCode.like(to))
        else:
            raise Exception("El parametro to tiene un formato incorrecto")

    if when:
        
        try:
            datef = datetime.datetime.strptime(when,"%Y-%m-%d")
         #   print(datef)
         #    filters.append(model.createAt == datef)
        except:
            raise Exception("El parametro when tiene un formato incorrecto")    

    if len(filters) == 0:
        trayectos = model.query.all()
        return trayectos
    
    trayectos = model.query.filter(and_(*filters)).all()

    return trayectos
    


def v_code(code):
    return re.match(r'\b[A-Z]{3}\b', code)


def se_puede_agregar_trayecto(trayecto, model) -> bool:

    date_pc = datetime.date.today()
   # print(date_pc)

    trayecto_buscado= model.query.filter(
        (model.sourceCountry == trayecto.sourceCountry) & 
        (model.destinyCountry == trayecto.destinyCountry)).all()

   # if len(trayecto_buscado) == 0:
    #    pass

    for tr in trayecto_buscado:
        date_ex = (tr.createAt + datetime.timedelta(30)).date()
     #   print(date_ex)
        if date_ex < date_pc:
            continue
        return False
    
    return True


def va_nombre_pais(nombre_pais):
    return re.match(r'[a-z]+(\s)?[a-z]*', nombre_pais, re.IGNORECASE)
