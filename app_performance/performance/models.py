from datetime import datetime, date
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()


class Performance(db.Model):

    __tablename__ = 'performance'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    candidate_id: int = db.Column(db.Integer)
    company_id: int = db.Column(db.Integer)
    project_id: int = db.Column(db.Integer)
    score: int = db.Column(db.Integer, nullable=True)
    feedback: str = db.Column(db.String(150), nullable=True)
    metrics: str = db.Column(db.String(150), nullable=True)
    createdAt: str = db.Column(db.Date, default=date.today())

class PerformanceaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Performance
    offer = fields.String()
    createdAt = fields.String()
