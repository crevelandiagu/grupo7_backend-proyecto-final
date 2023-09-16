# Gestion de Trayectos

## Descripción

El microservicio de gestión de trayectos permite crear trayectos (rutas) para ser usados por las publicaciones.


# Estructura
````
├── servicio_trayectos
|   └── trayectos
|   |   └── __init__.py
|   |   └── core.py
|   |   └── model.py
|   |   └── views.py
|   └── Dockerfile
|   └── README.md # Estás aquí
|   └── app.py
|   └── requirements.txt
|   └── test_trayectos.py
└──-└── wsgi.py
````

**servicio_trayectos:** Contiene todos los recursos del componente trayectos.
**trayectos:** Continen los fuentes principales del componenete.
**core.py:** Define la lógica que resuelve los llamados al API.
**model.py:** Define el modelado de la entidad Publicació.
**view.py:** Define de rutas del API.
**Dockerfile:** Contiene definicion para creacion de imagen.
**test_trayectos.py:** Contiene las pruebas unitarias del componenete.

## Como ejecutar localmente el servicio

1. Situarse en servicio_trayectos
2. Crear y activar entorno virtual env
3. Instalar dependencias
3. Subir servicio
```
cd ./servicio_trayectos/
python3 -m venv ./
source ./venv/Scripts/activate
pip install -r requirements.txt
flask run 
```

## Como ejecutar localmente las pruebas

1. Situarse en el servicio_trayectos
2. Crear y activar entorno virtual env
3. Ejecutar pruebas
```
cd ./servicio_trayectos/
python3 -m venv ./
source ./venv/Scripts/activate
pip install -r requirements.txt
pytest --cov=src -v -s --cov-fail-under=80
```

## Como ejecutar docker del servicio

1. Construir imagen
2. Ejecutar contenedor

```
cd ./servicio_trayectos/
docker build -t trayectos ./
docker run -d trayectos -p 5002:5002

```
