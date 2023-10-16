from .handlers import (endpoint_offers,
                       endpoint_posts,
                       endpoint_journey,
                       endpoint_users)


def creacion_publicacion(request):
    try:
        planned_start_date = request.json["plannedStartDate"]
        planned_end_date = request.json["plannedEndDate"]
        origin_airport_code = request.json["origin"]["airportCode"]
        origin_country = request.json["origin"]["country"]
        destiny_airport_code = request.json["destiny"]["airportCode"]
        destiny_country = request.json["destiny"]["country"]
        bag_cost = request.json["bagCost"]
    except Exception as e:
        return {"mensaje":f"Todos los campos son obligatorios:: {e}"}, 400
    
    search_route_status, search_route_data = endpoint_journey(
        headers=request.headers,
        method='GET',
        ruta=f'/routes?from={origin_airport_code}&to={destiny_airport_code}',
        data= {})
    
    if search_route_status != 200:
        return search_route_data, search_route_status
    
    if len(search_route_data) == 0:
        create_route_status, create_route_data = endpoint_journey(
            headers=request.headers,
            method='POST',
            ruta='/routes/',
            data={
                "sourceAirportCode":origin_airport_code,
                "sourceCountry":origin_country,
                "destinyAirportCode":destiny_airport_code,
                "destinyCountry":destiny_country,
                "bagCost":bag_cost
            })

        if create_route_status == 201:
            route_id=create_route_data[0]["id"]
            route_create_at = create_route_data[0]["createAt"]
            route_expire_at = create_route_data[0]["expireAt"]
        else:
            return create_route_data, create_route_status
        
    elif len(search_route_data) >= 1:
        route_id=search_route_data[0]["id"]
        route_create_at = search_route_data[0]["createAt"]
        route_expire_at = search_route_data[0]["expireAt"]

        search_post_status, search_post_data = endpoint_posts(
            headers=request.headers,
            method='GET',
            ruta=f'/posts?when={planned_start_date}&route={route_id}&filter=me',
            data={}
        )
    
        if search_post_status == 200 and len(search_post_data) > 0 :
            return {"msg":"El usuario ya tiene una publicación para la misma fecha"}, 412
    
    create_post_status, create_post_data = endpoint_posts(
        headers=request.headers,
        method='POST',
        ruta='/posts/',
        data={
                "routeId": route_id,
                "plannedStartDate": planned_start_date,
                "plannedEndDate": planned_end_date
            })
    
    if(create_post_status != 201):
        endpoint_journey(
            headers=request.headers,
            method='DELETE',
            ruta=f'/routes/{route_id}',
            data={})
        
        return {"msg":"Las fechas no son válidas"}, 412
    else:
        return {
            "data": {
                "id": create_post_data["id"],
                "userId": create_post_data["userId"],
                "createdAt": create_post_data["createdAt"],
                "route": {
                    "id": route_id,
                    "createdAt": route_create_at,
                    "expireAt": route_expire_at
                }
            },
            "msg": "Post created"
        }, 201

def creacion_oferta_publicacion(request, id):

    # Consultar el usuario de la petición
    user = endpoint_users(
        headers=request.headers,
        method='GET',
        ruta='/app_company/me',
        data={})
    if user[0]!=200:
        return user[1], user[0]
    user_offer_id = user[1].get('id', -1)

    # Consultar la publicación
    try:
        id= int(id)
    except Exception as e:
        return {"msg":"PostId must be a number"}, 412
    
    publicacion = endpoint_posts(
                    headers=request.headers,
                    method='GET',
                    ruta=f'posts/{id}',
                    data={})
    if publicacion[0]!=200:
        return publicacion[1], publicacion[0]
    user_publicacion_id = publicacion[1].get('userId', -1)

    # Validar usuario
    if (user_publicacion_id == user_offer_id):
        return {"msg":"You can't create app_performance for your own posts"}, 412

    # Crear la oferta
    try:
        data = request.json
        data.update({"postId": id})
        offer = endpoint_offers(headers=request.headers,
                                method='POST',
                                ruta ='app_performance/',
                                data=data)
        if offer[0] != 201:
            return offer[1] , offer[0]
        return {
                    "data": offer[1],
                    "msg": "The offer was successfully created."
                }, 201

    except Exception as e:
        print(e)
        return {"msg": f"Error {e} was found"}, 400


def consultar_publicacion(request, id):
    # primero consultamos publicacion
    publicacion = endpoint_posts(
                    headers=request.headers,
                    method='GET',
                    ruta=f'posts/{id}',
                    data={})
    if publicacion[0] != 200:
        return publicacion[1], publicacion[0]
    # permisos
    user = endpoint_users(
        headers=request.headers,
        method='GET',
        ruta='/app_company/me',
        data={})
    if publicacion[0] != 200:
        return user[1], user[0]

    if publicacion[1].get('userId', -1) != user[1].get('id', -1):
        return {"mensaje": f"Usuario no autorizado"}, 403
    # segudno consultamos las rutas
    rutas_id = publicacion[1].get('routeId', -1)
    trayecctos = endpoint_journey(
                    headers=request.headers,
                    method='GET',
                    ruta=f'routes/{rutas_id}',
                    data={})
    if trayecctos[0] != 200:
        return trayecctos[1], trayecctos[0]

    trayecctos_data = trayecctos[1][0]
    # tercera consulta las payments
    datos_ofertas_publicacion = endpoint_offers(
                    headers=request.headers,
                    method='GET',
                    ruta=f'app_performance/',
                    data={})
    if datos_ofertas_publicacion[0] != 200:
        return datos_ofertas_publicacion[1], datos_ofertas_publicacion[0]

    bagCost = float(trayecctos_data.get('bagCost', -1))

    # ofertar desendente por utilidad
    # valor de de la utilidad con el detalle de cada oferta
    ofertas_publicaciones = [completar_oferta(i, bagCost)for i in datos_ofertas_publicacion[1] if i.get('postId', 0) == id]
    ofertas_publicaciones_ordenada = sorted(ofertas_publicaciones, key=lambda k: k['score'], reverse=True)

    return orgazinar_data_consultar_publicacion(publicacion[1],
                                         trayecctos_data,
                                         ofertas_publicaciones_ordenada), 200

def completar_oferta(data, bagCost):
    ocupacion_maleta_tamano = data.get('size', 'none')
    porcentaje_maleta = {'LARGE': 1,
                         'MEDIUM': 0.5,
                         'SMALL': 0.25,
                         'none': 0}
    ocupacion_maleta = porcentaje_maleta[ocupacion_maleta_tamano]
    score = float(data.get('offer', 0)) - (bagCost*ocupacion_maleta)
    data.update({'score': score})
    data.pop('postId')
    return data

def orgazinar_data_consultar_publicacion(publicacion,
                                         trayecctos_data,
                                         ofertas_publicaciones_ordenada):

    return {
        "data": {
            "id": publicacion['id'],
            "route": {
                "id": trayecctos_data['id'],
                "origin": {
                    "airportCode": trayecctos_data['sourceAirportCode'],
                    "country": trayecctos_data['sourceCountry']
                },
                "destiny": {
                    "airportCode": trayecctos_data['destinyAirportCode'],
                    "country": trayecctos_data['destinyCountry']
                },
                "bagCost": trayecctos_data['bagCost']
            },
            "plannedStartDate": publicacion['plannedEndDate'],
            "plannedEndDate": publicacion['plannedStartDate'],
            "createdAt": publicacion['createdAt'],
            "app_performance": ofertas_publicaciones_ordenada
        }
    }

