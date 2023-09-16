import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def valid_date():
    date = datetime.date.today()
    return date


class Trayecto(db.Model):
    __tablename__ = "project"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sourceAirportCode: str = db.Column(db.String(200), unique=False, nullable=False)
    sourceCountry: str = db.Column(db.String(200), unique=False, nullable=False)
    destinyAirportCode: str = db.Column(db.String(200), unique=False, nullable=False)
    destinyCountry: str = db.Column(db.String(200), unique=False, nullable=False)
    bagCost: float = db.Column(db.Numeric(precision=7, scale=2), nullable=False)
    createAt: datetime = db.Column(db.DateTime, nullable=False, default=valid_date)


