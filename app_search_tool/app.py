import os
from flask import Flask
from flask_cors import CORS
from search_tool import search_tool
# from search_tool.connection_db import db
from flask_jwt_extended import JWTManager
from flask_openapi3 import Info
from flask_openapi3 import OpenAPI

ACTIVATE_ENDPOINTS = (('/', search_tool),)

info = Info(title="Search Tool API", version="1.3.0")

app = OpenAPI(__name__,
              info=info,
              doc_prefix="/search-tool/docs"
              )

app.secret_key = 'dev'

app.url_map.strict_slashes = False

dbname = os.getenv('DB_NAME', 'search_tool_db')
url_posgres = os.getenv('DATABASE_URL', 'postgresql://postgres:postgres@localhost:5432/')

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'frase-secreta'
app.config['PROPAGATE_EXCEPTIONS'] = True

# db.init_app(app)
#
# with app.app_context():
#     db.create_all()

app_context = app.app_context()
app_context.push()
cors = CORS(app, resources={r"*": {"origins": "*"}})


for url, blueprint in ACTIVATE_ENDPOINTS:
    app.register_api(blueprint)

jwt = JWTManager(app)


