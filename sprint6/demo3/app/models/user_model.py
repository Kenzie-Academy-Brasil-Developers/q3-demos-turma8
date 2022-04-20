from dataclasses import dataclass

from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from app.configs.database import db
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash


@dataclass
class User(db.Model):
    user_id: str
    email: str
    api_key: str
    # unsafe_password: str

    __tablename__ = 'users'
    # user_id = Column(Integer, primary_key=True)
    # UUID
    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    email = Column(String(64), unique=True, nullable=False)
    # unsafe_password = Column(String, nullable=False)
    password_hash = Column(String)
    api_key = Column(String)

    """
        {
            "email": "alguma_coisa@mail.com",
            "password": "1234"
        }
    """

    """
        user -> objeto da classe User
        print(user.password)
        AttributeError
    """

    @property
    def password(self):
        raise AttributeError('Não é possivel acessar o atributo password')

    """
        user.password = '1234'
    """

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)

    def check_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)
