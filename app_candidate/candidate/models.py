import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Candidates(db.Model):

    __tablename__ = 'candidate'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(150), nullable=False)
    username: str = db.Column(db.String(150))
    email: str = db.Column(db.String(150))

    cv_file: str = db.Column(db.String(150), nullable=False)
    score: str = db.Column(db.String(5), nullable=False)
    payment_id: str = db.Column(db.String(150), nullable=False)
    status: str = db.Column(db.String(150), nullable=False)
    choose_one: str = db.Column(db.String(150), nullable=False)
    course_id: str = db.Column(db.String(150), nullable=False)

    cv: int = db.Column(db.Integer, db.ForeignKey('curriculum_vitae.id'))

    password: str = db.Column(db.Text)
    salt: str = db.Column(db.String(150))
    createdAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)
    updatedAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)


class CurriculumVitae(db.Model):

    __tablename__ = 'curriculum_vitae'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    skills: str = db.Column(db.String(150), nullable=False)
    my_profile: str = db.Column(db.String(150), nullable=False)
    work_experience: str = db.Column(db.String(150), nullable=False)
    education: str = db.Column(db.String(150), nullable=False)
    administrative_data: str = db.Column(db.String(500), nullable=True)
    createdAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)
    updatedAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)

    candidate_id = db.relationship('Candidates', cascade='all, delete, delete-orphan')
