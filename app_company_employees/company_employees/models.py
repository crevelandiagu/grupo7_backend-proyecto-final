import datetime
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


db = SQLAlchemy()


class EmployeeCompany(db.Model):

    __tablename__ = 'employees_company'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(150), nullable=True)
    seniority: str = db.Column(db.String(150), nullable=True)
    company_id: int = db.Column(db.Integer)
    company_project_id: int = db.Column(db.Integer, nullable=True)

    project_interview_id = db.relationship('ProjectInterview', cascade='all, delete, delete-orphan')

    email: str = db.Column(db.String(150))
    password: str = db.Column(db.Text)
    salt: str = db.Column(db.String(150))
    createdAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)
    updatedAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)


class ProjectInterview(db.Model):

    __tablename__ = 'project_interview'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)

    employees_company_id: int = db.Column(db.Integer, db.ForeignKey('employees_company.id'))

    interview_process_id = db.relationship('InterviewProcess', cascade='all, delete, delete-orphan')

    createdAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)
    updatedAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)


class InterviewProcess(db.Model):

    __tablename__ = 'interview_process'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status: str = db.Column(db.String(150), nullable=True)
    company_id: int = db.Column(db.Integer, nullable=True)
    project_interview_id: int = db.Column(db.Integer, db.ForeignKey('project_interview.id'))

    createdAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)
    updatedAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)


