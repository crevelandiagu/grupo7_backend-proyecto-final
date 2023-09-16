from datetime import datetime, date
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()


class Oferta(db.Model):

    __tablename__ = 'payments'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    postId: int = db.Column(db.Integer)
    userId: int = db.Column(db.Integer)
    description: str = db.Column(db.String(140))
    size: str = db.Column(db.String(150))
    fragile: str = db.Column(db.Boolean)
    offer: str = db.Column(db.Integer)
    createdAt: str = db.Column(db.Date, default=date.today())

class OfertaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Oferta
    offer = fields.String()
    createdAt = fields.String()
