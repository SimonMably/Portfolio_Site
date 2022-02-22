from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import query
from portfolio_site import db

class Admin(UserMixin, db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))


class Portfolio(db.Model):
    __tablename__ = "portfolio"
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(100), unique=True, nullable=False)
    project_description = db.Column(db.String(500), nullable=False)
    project_url = db.Column(db.String(300), nullable=False)
    img_name = db.Column(db.String(300), nullable=False)
    made_with = db.Column(db.String(300), nullable=False)

    def __repr__(self) -> str:
        return f"{self.project_name}"
    
db.create_all()