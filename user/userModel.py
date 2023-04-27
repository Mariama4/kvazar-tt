from dataclasses import dataclass
from datetime import datetime
from db import db


@dataclass
class UserModel(db.Model):
    """User Model"""

    __tablename__ = "User"

    id: db.Column[db.Integer] = db.Column(db.Integer, primary_key=True)
    username: db.Column[str] = db.Column(db.String(45), unique=True, nullable=False)
    email: db.Column[str] = db.Column(db.String(45), unique=True, nullable=False)
    registration_date: db.Column[datetime] = db.Column(
        db.DateTime, default=datetime.now()
    )
