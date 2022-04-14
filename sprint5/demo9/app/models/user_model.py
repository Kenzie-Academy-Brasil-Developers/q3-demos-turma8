from app.configs.database import db

from sqlalchemy import BigInteger, Boolean, Column, Date, Integer, Numeric, String
from sqlalchemy.orm import relationship, validates
from dataclasses import dataclass
from app.exc import InvalidEmailError, InvalidDateFormatError
from datetime import datetime as dt


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
    # created_at -> Date

    orders = relationship("Order", back_populates="customer", uselist=True)

    @validates("email")
    def validate_email(self, key, email_to_be_tested):
        print(f"{key=}")
        if "churros" not in email_to_be_tested:
            raise InvalidEmailError

        return email_to_be_tested.title()

    @validates("birthdate")
    def validate_birthdate(self, key, date_to_be_tested):
        try:
            b_date = dt.strptime(date_to_be_tested, "%Y/%m/%d")
        except ValueError:
            raise InvalidDateFormatError
        # TODO:
        # Adicionar uma testagem para barrar pessoais com menos de 25 anos

        return date_to_be_tested
