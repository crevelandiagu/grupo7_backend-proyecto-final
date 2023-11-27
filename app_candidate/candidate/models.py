import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSONB

db = SQLAlchemy()


class Candidates(db.Model):

    __tablename__ = 'candidate'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(150), nullable=True)
    lastname: str = db.Column(db.String(150), nullable=True)
    email: str = db.Column(db.String(150))
    birthdate: str = db.Column(db.String(150), nullable=True)
    nacionality: str = db.Column(db.String(150), nullable=True)
    phone_number: str = db.Column(db.String(150), nullable=True)
    number_id: str = db.Column(db.String(150), nullable=True)
    score: str = db.Column(db.String(5), nullable=True)
    payment_id: str = db.Column(db.String(150), nullable=True)

    status: str = db.Column(db.String(150), nullable=True)
    choose_one: str = db.Column(db.Boolean, default=False, nullable=True)
    course_id: str = db.Column(db.String(150), nullable=True)

    cv_experience_id = db.relationship('CvExperience', cascade='all, delete, delete-orphan')
    cv_education_id = db.relationship('CvEducation', cascade='all, delete, delete-orphan')
    cv_certificates_id = db.relationship('CvCertificates', cascade='all, delete, delete-orphan')
    cv_skills_id = db.relationship('CvSkills', cascade='all, delete, delete-orphan')

    password: str = db.Column(db.Text)
    salt: str = db.Column(db.String(150))
    createdAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)
    updatedAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)


class CvExperience(db.Model):

    __tablename__ = 'cv_experience'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    experience = db.Column(JSONB, nullable=True)
    createdAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)
    updatedAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)

    candidate_id: int = db.Column(db.Integer, db.ForeignKey('candidate.id'))



class CvEducation(db.Model):

    __tablename__ = 'cv_education'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    education = db.Column(JSONB, nullable=True)
    createdAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)
    updatedAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)

    candidate_id: int = db.Column(db.Integer, db.ForeignKey('candidate.id'))



class CvCertificates(db.Model):

    __tablename__ = 'cv_certificates'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    certificates = db.Column(JSONB, nullable=True)
    createdAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)
    updatedAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)

    candidate_id: int = db.Column(db.Integer, db.ForeignKey('candidate.id'))

class CvSkills(db.Model):

    __tablename__ = 'cv_skills'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    skills = db.Column(JSONB, nullable=True)
    years_exp: float = db.Column(db.Numeric, nullable=True, default=0)
    name: str = db.Column(db.String(150), nullable=True)
    lastname: str = db.Column(db.String(150), nullable=True)
    choose_one: str = db.Column(db.Boolean, default=False, nullable=True)
    createdAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)
    updatedAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)

    candidate_id: int = db.Column(db.Integer, db.ForeignKey('candidate.id'))
