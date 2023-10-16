from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


db = SQLAlchemy()



class Publicacion(db.Model):

    __tablename__ = 'company_employees'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    routeId: int = db.Column(db.Integer)
    userId: int = db.Column(db.Integer)
    plannedStartDate: datetime = db.Column(db.DateTime)
    plannedEndDate: datetime = db.Column(db.DateTime)
    createdAt: datetime = db.Column(db.DateTime, default=datetime.now())

class PublicacionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Publicacion
