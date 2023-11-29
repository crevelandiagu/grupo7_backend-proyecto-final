# Descripcion estructura componente publicaciones

En este proyecto se encuentra el código de ejemplo para ejecutar un pipeline de github que valida que el código esté cubierto en un mínimo de 80% en pruebas.

Este proyecto hace uso de pip para gestión de dependencias y pytest para el framework de pruebas.

# Estructura
````
├── servicio_publicaciones
|   └── publicaciones
|   |   └── __init__.py
|   |   └── core.py
|   |   └── model.py
|   |   └── views.py
|   └── Dockerfile
|   └── README.md # Estás aquí
|   └── app.py
|   └── requirements.txt
|   └── test_publicaciones.py
└──-└── wsgi.py
````

**servicio_publicaciones:** Contiene todos los recursos del componente publiacion.
**publicaciones:** Continen los fuentes principales del componenete.
**core.py:** Define la lógica que resuelve los llamados al API.
**model.py:** Define el modelado de la entidad Publicació.
**view.py:** Define de rutas del API.
**Dockerfile:** Contiene definicion para creacion de imagen.
**test_publicaciones.py:** Contiene las pruebas unitarias del componenete.

## Como ejecutar localmente el servicio

1. Situarse en servicio_publicaciones
2. Crear y activar entorno virtual env
3. Instalar dependencias
3. Subir servicio
```
cd ./servicio_publicaciones/
python3 -m venv ./
source ./venv/Scripts/activate
pip install -r requirements.txt
flask run 
```

## Como ejecutar localmente las pruebas

1. Situarse en el servicio_publicaciones
2. Crear y activar entorno virtual env
3. Ejecutar pruebas
```
cd ./servicio_publicaciones/
python3 -m venv ./
source ./venv/Scripts/activate
pip install -r requirements.txt
pytest --cov=src -v -s --cov-fail-under=80
```

## Como ejecutar docker del servicio

1. Construir imagen
2. Ejecutar contenedor

```
cd ./servicio_publicaciones/
docker build -t publicaciones ./
docker run -d publicaciones -p 5001:5001
```