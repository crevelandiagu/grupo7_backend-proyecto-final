import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Candidates(db.Model):

    __tablename__ = 'candidate'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(150), nullable=True)
    lastname: str = db.Column(db.String(150), nullable=True)
    email: str = db.Column(db.String(150))
    birthdate: str = db.Column(db.String(150), nullable=True)
    nacionality: str = db.Column(db.String(150), nullable=True)

    cv_file: str = db.Column(db.String(150), nullable=True)
    score: str = db.Column(db.String(5), nullable=True)
    payment_id: str = db.Column(db.String(150), nullable=True)
    status: str = db.Column(db.String(150), nullable=True)
    choose_one: str = db.Column(db.Boolean, default=False, nullable=True)
    course_id: str = db.Column(db.String(150), nullable=True)

    cv: int = db.Column(db.Integer, db.ForeignKey('curriculum_vitae.id'))

    password: str = db.Column(db.Text)
    salt: str = db.Column(db.String(150))
    createdAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)
    updatedAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)


class CurriculumVitae(db.Model):

    __tablename__ = 'curriculum_vitae'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    skills: str = db.Column(db.String(400), nullable=True)
    my_profile: str = db.Column(db.String(400), nullable=True)
    work_experience: str = db.Column(db.String(400), nullable=True)
    education: str = db.Column(db.String(400), nullable=True)
    certificates: str = db.Column(db.String(400), nullable=True)
    administrative_data: str = db.Column(db.String(500), nullable=True)
    createdAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)
    updatedAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)

    candidate_id = db.relationship('Candidates', cascade='all, delete, delete-orphan')
