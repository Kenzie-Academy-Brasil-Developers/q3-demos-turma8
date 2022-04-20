from flask import Blueprint
from app.controllers import home_controller

bp = Blueprint('home', __name__, url_prefix='/home')

bp.get('')(home_controller.home)