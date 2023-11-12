import datetime
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


db = SQLAlchemy()


class Projects(db.Model):

    __tablename__ = "project"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    projectName: str = db.Column(db.String(200), unique=False, nullable=False)
    description: str = db.Column(db.String(400), unique=False, nullable=True)
    status: str = db.Column(db.String(100), unique=False, nullable=True)
    companyId: int = db.Column(db.Integer, nullable=False)
    createdAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)

    candidate_project_id = db.relationship('CandidateProject', cascade='all, delete, delete-orphan')
    project_employees_companie_id = db.relationship('ProjectEmployeesCompanie', cascade='all, delete, delete-orphan')


class CandidateProject(db.Model):

    __tablename__ = 'candidate_project'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)

    project_id: int = db.Column(db.Integer, db.ForeignKey('project.id'))
    candidate_id: int = db.Column(db.Integer)
    data: str = db.Column(db.String(500),  unique=False, nullable=True)

    createdAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)
    updatedAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)


class ProjectEmployeesCompanie(db.Model):

    __tablename__ = 'project_employees_companie'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)

    project_id: int = db.Column(db.Integer, db.ForeignKey('project.id'))
    employees_id: int = db.Column(db.Integer)
    data: str = db.Column(db.String(500),  unique=False, nullable=True)

    createdAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)
    updatedAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)


# class ProjectEmployees(db.Model):
#
#     __tablename__ = 'project_employees'
#     id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
#
#     project_employees_id: int = db.Column(db.Integer, db.ForeignKey('project_employees_companie.id'))
#     employees_id: int = db.Column(db.Integer)
#
#     createdAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)
#     updatedAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)


class ProjectsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Projects
        include_relationships = True
        include_fk = True
        load_instance = True
