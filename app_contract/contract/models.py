from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


db = SQLAlchemy()



class Publicacion(db.Model):

    __tablename__ = 'company_employees'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    candidateId: int = db.Column(db.Integer)
    projectId: int = db.Column(db.Integer)
    companyId: int = db.Column(db.Integer)
    data: str = db.Column(db.String(500), unique=False, nullable=True)
    createdAt: datetime = db.Column(db.DateTime, default=datetime.now())

class PublicacionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Publicacion

