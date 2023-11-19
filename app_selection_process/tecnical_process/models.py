# import datetime
# from flask_sqlalchemy import SQLAlchemy
# # from sqlalchemy.dialects.postgresql import JSONB
# # from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
# # # from app_selection_process.interview_process.models import db_interview
# #
# db_assement = SQLAlchemy()
# db = db_assement
# #
#
# class Assement(db.Model):
#
#     __tablename__ = 'assement'
#     id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     candidate_name: str = db.Column(db.String(150))
#     candidate_id: int = db.Column(db.Integer)
#     company_id: int = db.Column(db.Integer)
#     score: str = db.Column(db.String(5), nullable=True)
#     project_id: int = db.Column(db.Integer)
#     status: str = db.Column(db.String(150), nullable=True)
#     createdAt: datetime = db.Column(db.DateTime, default=datetime.datetime.now)
# #
# # class AssementSchema(SQLAlchemyAutoSchema):
# #     class Meta:
# #         model = Assement
# #         include_relationships = True
# #         include_fk = True
# #         load_instance = True