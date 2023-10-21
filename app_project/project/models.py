import datetime
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


db = SQLAlchemy()



class Projects(db.Model):
    __tablename__ = "project"
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    projectName: str = db.Column(db.String(200), unique=False, nullable=False)
    description: str = db.Column(db.String(400), unique=False, nullable=True)
    companyId: int =db.Column(db.Integer, nullable=False)   
    createdAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)

class ProjectsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Projects
        include_relationships = True
        include_fk = True
        load_instance = True
