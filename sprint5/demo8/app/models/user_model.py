from app.configs.database import db

from sqlalchemy import BigInteger, Boolean, Column, Date, Integer, Numeric, String
from sqlalchemy.orm import relationship
from dataclasses import dataclass


@dataclass
class User(db.Model):
    user_id: int
    email: str
    birthdate: str
    children: int
    married: bool
    account_balance: float
    # orders: list

    __tablename__ = "users"

    user_id = Column(BigInteger, primary_key=True)
    email = Column(String(64), unique=True, nullable=False)
    birthdate = Column(Date, nullable=False)
    children = Column(Integer, default=0)
    married = Column(Boolean, default=False)
    account_balance = Column(Numeric(asdecimal=False))

    orders = relationship("Order", back_populates="customer", uselist=True)
