import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSONB
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()


class Interview(db.Model):

    __tablename__ = 'interview'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_interview: datetime = db.Column(db.DateTime)
    candidate_name: str = db.Column(db.String(150))
    candidate_id: int = db.Column(db.Integer)
    company_id: int = db.Column(db.Integer)
    company_employee_id: int = db.Column(db.Integer)
    score: str = db.Column(db.String(5), nullable=True)
    project_id: int = db.Column(db.Integer)
    status: str = db.Column(db.String(150), nullable=True)
    createdAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)

class InterviewSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Interview
        include_relationships = True
        include_fk = True
        load_instance = True


class Assement(db.Model):

    __tablename__ = 'assement'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    candidate_id: int = db.Column(db.Integer)
    company_id: int = db.Column(db.Integer)
    project_id: int = db.Column(db.Integer)
    score: int = db.Column(db.Integer, nullable=True)
    status: str = db.Column(db.String(150), nullable=True)
    assement_id: int = db.Column(db.Integer)
    data: str = db.Column(db.String(500), nullable=True)
    createdAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)

class AssementSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Assement
