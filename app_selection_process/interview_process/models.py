import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSONB
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class SelectionProcess(db.Model):

    __tablename__ = 'selection_process'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pogress_status: str = db.Column(db.String(150))

    candidate_id: int = db.Column(db.Integer)
    candidate_name: str = db.Column(db.String(150))

    project_id: int = db.Column(db.Integer)
    project_name: str = db.Column(db.String(150))

    company_id: int = db.Column(db.Integer)
    company_name: str = db.Column(db.String(150))

    score: str = db.Column(db.String(5), nullable=True)
    createdAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)


class SelectionProcessSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = SelectionProcess
        include_relationships = True
        include_fk = True
        load_instance = True

class Interview(db.Model):

    __tablename__ = 'interview'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_interview: datetime = db.Column(db.DateTime)

    candidate_id: int = db.Column(db.Integer)
    candidate_name: str = db.Column(db.String(150))

    project_id: int = db.Column(db.Integer)
    project_name: str = db.Column(db.String(150))

    company_id: int = db.Column(db.Integer)
    company_name: str = db.Column(db.String(150))


    company_employee_id: int = db.Column(db.Integer)
    score: str = db.Column(db.String(5), nullable=True)

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
    candidate_name: str = db.Column(db.String(150))

    project_id: int = db.Column(db.Integer)
    project_name: str = db.Column(db.String(150))

    company_id: int = db.Column(db.Integer)
    company_name: str = db.Column(db.String(150))

    score: int = db.Column(db.Integer)
    status: str = db.Column(db.String(150), nullable=True)
    test_id: int = db.Column(db.Integer)

    createdAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)


class AssementSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Assement
        include_relationships = True
        include_fk = True
        load_instance = True