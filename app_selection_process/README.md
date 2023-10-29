# Servicios de selección de candidatos


En esta carpeta se encuentra el código de public el cual utiliza el patron saga. Este microservicio ofrece un punto de acceso al sistema y hace una sola petición web por cada requerimiento y no una secuencia.

Este proyecto hace uso de pipenv para gestión de dependencias y pytest para el framework de pruebas.

# Estructura

````
├── public                   # Archivos de la aplicación de public 
|   ├── publico              # Código que contiene la logica de la aplicación
|   |    ├── __init__.py     # Inicia las rutas para acceder a las urls
|   |    ├── core.py         # Contiene las validaciones y logica de public
|   |    ├── handlers.py     # Contiene funciones de logica de public
|   |    ├── views.py        # Contiene las vistas de las diferentes funcionalidades 
|   ├── app.py               # Inio de la aplicacion de flask y su configuracion
|   ├── Dockerfile           # Archivo de configuracion de la imagen de la aplicación
|   ├── README.md            # Estás aquí
|   ├── requirements.txt     # Dependencias de la aplicación
|   ├── test_public_posts.py # Paquete de pruebas publicaciones
|   ├── test_rf004.py        # Paquete de pruebas ofertas
|   ├── test_rf005.py        # Paquete de pruebas ofertas
|   └── wsgi.py              # Punto de inicio de la aplicacion con gunicorn 
````

## Despliegue local de la aplicación

1. Creacion de entorno virtual
```shell
    python3 -m venv env
```
2. Instalacion de dependencias 
```shell
   pip3 install -r requirements.txt 
```
3. Ejecutar el comando
```shell
    gunicorn --reload wsgi:app --bind 0.0.0.0:3000 --log-level debug
```
### Despliegue con Dockerfile

1. Comandos de docker para desplegar el docker file
```shell
    docker build -t app-interview_process .
```
2. Comandos de docker despues de que se crea la imagen
```shell
    docker run -p 8000:5000 -it app-interview_process
```

## Como ejecutar localmente las pruebas

1. Corriendo los test
```shell
  pytest
```
2. Corriendo el coverage 
```shell
  pytest --cov=. -v -s --cov-fail-under=80
```
