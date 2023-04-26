from db import db
from datetime import datetime
from dataclasses import dataclass


@dataclass
class UserModel(db.Model):
    """User Model"""

    __tablename__ = "User"

    id: db.Column[db.Integer] = db.Column(db.Integer, primary_key=True)
    username: db.Column[db.String] = db.Column(db.String(45), nullable=False)
    email: db.Column[db.String] = db.Column(db.String(45), unique=True, nullable=False)
    registration_date: db.Column[db.DateTime] = db.Column(
        db.DateTime, default=datetime.now
    )
