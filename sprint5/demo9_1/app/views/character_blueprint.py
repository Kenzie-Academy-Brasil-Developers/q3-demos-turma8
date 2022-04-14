from flask import Blueprint, render_template
from app.services import retrieve_rick_and_morty_images

bp = Blueprint("characters", __name__, url_prefix="/characters")


@bp.get("")
def home():
    chars_images = retrieve_rick_and_morty_images()
    # print(chars_images)
    return render_template("character.html", images=chars_images)
