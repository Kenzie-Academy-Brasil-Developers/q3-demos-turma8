from sqlalchemy import Column, String, Integer
from app.configs.database import db


class User(db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    login = Column(String, nullable=False)
    credit_card_number = Column(String, nullable=False, unique=True)
    provider = Column(String(50), nullable=False)
    security_code = Column(String(3), nullable=False)
    expire_date = Column(String, nullable=False)
