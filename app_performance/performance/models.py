from datetime import datetime, date
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()


class Performance(db.Model):

    __tablename__ = 'performance'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    candidateId: int = db.Column(db.Integer)
    companyId: int = db.Column(db.Integer)
    projectId: int = db.Column(db.Integer)

    candidate_name: str = db.Column(db.String(150))
    project_name: str = db.Column(db.String(150))
    company_name: str = db.Column(db.String(150))

    employees: str = db.Column(db.String(600))
    score: int = db.Column(db.Integer, nullable=True)
    feedback: str = db.Column(db.String(150), nullable=True)
    metrics: str = db.Column(db.String(150), nullable=True)
    createdAt: str = db.Column(db.Date, default=date.today())

class PerformanceaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Performance

