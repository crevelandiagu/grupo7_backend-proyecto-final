import os
from flask import Flask
from flask_cors import CORS
from company import company
from company.models import db
from flask_jwt_extended import JWTManager
from flask_openapi3 import Info
from flask_openapi3 import OpenAPI

ACTIVATE_ENDPOINTS = (('/', company),)

info = Info(title="Company API", version="0.2.2")

app = OpenAPI(__name__,
              info=info,
              doc_prefix="/company/docs"
              )

app.secret_key = 'dev'

app.url_map.strict_slashes = False

dbname = os.getenv('DB_NAME', 'company_db')
url_posgres = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/')

if os.getenv('TEST_APP'):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = f"{url_posgres}{dbname}"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'frase-secreta'
app.config['PROPAGATE_EXCEPTIONS'] = True


db.init_app(app)

with app.app_context():
    db.create_all()

app_context = app.app_context()
app_context.push()
cors = CORS(app, resources={r"*": {"origins": "*"}})



for url, blueprint in ACTIVATE_ENDPOINTS:
    app.register_api(blueprint)

jwt = JWTManager(app)


