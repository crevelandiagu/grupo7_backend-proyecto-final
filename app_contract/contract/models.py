from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


db = SQLAlchemy()


class Contract(db.Model):

    __tablename__ = 'contract'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    candidateId: int = db.Column(db.Integer)
    projectId: int = db.Column(db.Integer)
    companyId: int = db.Column(db.Integer)
    createdAt: datetime = db.Column(db.DateTime, default=datetime.now())



