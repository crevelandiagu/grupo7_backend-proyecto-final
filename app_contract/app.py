import os
from flask import Flask
from flask_cors import CORS
from contract import publicaciones
from contract.models import db


ACTIVATE_ENDPOINTS = (('/', publicaciones),)


app = Flask(__name__)
app.secret_key = 'dev'

app.url_map.strict_slashes = False

username = os.getenv('DB_USER', 'admin')
password = os.getenv('DB_PASSWORD', 'admin')
dbname = os.getenv('DB_NAME', 'publicaciones_db')
hostname = os.getenv('DB_HOST', 'db_publicaciones')
url_posgres = os.getenv('DATABASE_URL', 'postgresql://admin:admin@db_publicaciones:5432/publicaciones_db')

if os.getenv('TEST_APP', False) == 'True':
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
    app.register_blueprint(blueprint, url_prefix=url)




