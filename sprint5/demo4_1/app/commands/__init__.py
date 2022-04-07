from flask import Flask
from .user_commands import hello_world_cli, users_cli


def init_app(app: Flask):
    app.cli.add_command(hello_world_cli())
    app.cli.add_command(users_cli())
