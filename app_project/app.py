import os
from flask import Flask
from flask_cors import CORS
from project import projects
from project.models import db
from flask_jwt_extended import JWTManager
from flask_openapi3 import Info
from flask_openapi3 import OpenAPI

ACTIVATE_ENDPOINTS = (('/', projects),)


info = Info(title="Candidate API", version="0.0.1")

app = OpenAPI(__name__,
              info=info,
              doc_prefix="/projects/docs"
              )

app.secret_key = 'dev'

app.url_map.strict_slashes = False


username = os.getenv('DB_USER', 'admin')
password = os.getenv('DB_PASSWORD', 'admin')
dbname = os.getenv('DB_NAME', 'trayectos_db')
hostname = os.getenv('DB_HOST', 'db_trayectos')
url_posgres = os.getenv('DATABASE_URL', 'postgresql://admin:admin@db_trayectos:5432/trayectos_db')

if os.getenv('TEST_APP', 'True') == 'True':
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = url_posgres
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'frase-secreta'
app.config['PROPAGATE_EXCEPTIONS'] = True

db.init_app(app)

with app.app_context():
    db.create_all()

app_context = app.app_context()
app_context.push()
cors = CORS(app)


for url, blueprint in ACTIVATE_ENDPOINTS:
    app.register_api(blueprint)

jwt = JWTManager(app)




