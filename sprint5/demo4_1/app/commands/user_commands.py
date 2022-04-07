from flask.cli import AppGroup
import click
from faker import Faker
from app.configs.database import db
from app.models.user_model import User
from sqlalchemy.orm.session import Session


def hello_world_cli():
    hello_group = AppGroup("hello", help="Dá boas vindas")

    @hello_group.command("greeting")
    def gretting_who():
        print(f"Olá, seja bem vindo")

    return hello_group


def users_cli():
    fake = Faker("pt_BR")
    user_group = AppGroup("users", help="Faz operações com a model User")

    @user_group.command("create")
    @click.argument("amount", type=int)
    def create_users(amount):
        session: Session = db.session

        users = [
            User(
                login=fake.name(),
                credit_card_number=fake.credit_card_number(),
                provider=fake.credit_card_provider(),
                expire_date=fake.credit_card_expire(),
                security_code=fake.credit_card_security_code()[:3],
            )
            for _ in range(amount)
        ]

        session.add_all(users)
        session.commit()

    return user_group
