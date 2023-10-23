import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Companies(db.Model):

    __tablename__ = 'companies'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(150), nullable=True)
    nit: str = db.Column(db.String(150), nullable=True)
    username: str = db.Column(db.String(150))
    email: str = db.Column(db.String(150))
    number_employees: int = db.Column(db.Integer, nullable=True)
    core: str = db.Column(db.String(150), nullable=True)
    senority: str = db.Column(db.String(150), nullable=True)
    projects_id = db.relationship('Projects', cascade='all, delete, delete-orphan')

    password: str = db.Column(db.Text)
    salt: str = db.Column(db.String(150))
    createdAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)
    updatedAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)



class Projects(db.Model):

    __tablename__ = 'projects'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_id: int = db.Column(db.Integer, db.ForeignKey('companies.id'))

    createdAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)
    updatedAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)
