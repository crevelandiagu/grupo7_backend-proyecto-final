# Servicios de candidato 

En este proyecto se encuentra el código de usuarios el cual permite crear un usuario con username
passwork y un email, acceder a su cuenta por medio del username y passwork, el cual le regrea un token 
que le permitira realizar las diferentes transacciones con: ofertas, publicaciones y trayectos, para el 
envio de paquetes a travez de maletas de viajeros confiables 

Este proyecto hace uso de pipenv para gestión de dependencias y pytest para el framework de pruebas.

# Estructura

````
├── users                  # Archivos de la aplicación de usuarios 
|   ├── usuarios           # Código que contiene la logica de la aplicación
|   |    ├── __init__.py   # Inicia las rutas para acceder a las urls
|   |    ├── core.py       # Contiene las validaciones y logica de usuarios
|   |    ├── models.py     # Contiene el modelo de la base de datos de usuarios
|   |    ├── views.py      # Contiene las vistas de las diferentes funcionalidades 
|   ├── app.py             # Inio de la aplicacion de flask y su configuracion
|   ├── Dockerfile         # Archivo de configuracion de la imagne de la aplicaicon
|   ├── README.md          # Estás aquí
|   ├── requirements.txt   # Dependencias de la aplicación
|   ├── test_usuariosapp.py # Paquete de pruebas
|   └── wsgi.py            # Punto de inicio de la aplicacion con gunicorn 
````

## Despliegue local de la palicacion

1. Creacion de entorno virtual
```shell
    python3 -m venv env
```
2. Instalacion de dependencias 
```shell
   pip3 install -r requirements.txt 
```
4. Levantar la base de datos de postgres del docker-compose
5. Ejecutar el comando
```shell
    gunicorn --reload wsgi:app --bind 0.0.0.0:3000 --log-level debug
```
### Despliegue con Dockerfile

1. Comandos de docker para desplegar el docker file
```shell
    docker build -t app-candidate .
```
2. Comandos de docker despues de que se crea la imagen
```shell
    docker run -p 8000:5000 -it app-candidate
```

## Como ejecutar localmente las pruebas

1. Corriendo los test
```shell
  pytest
```
2. Corriendo el coverage 
```shell
  pytest --cov=. -v -s --cov-fail-under=70
```