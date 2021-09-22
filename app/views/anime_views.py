from flask import Blueprint
from app.services.anime_services import Animes

bp_animes = Blueprint("anime_bp", __name__, url_prefix="/animes")


@bp_animes.route("", methods=("GET", "POST"))
def get_create():
    anime = Animes()

    return {"msg": "ok"}


@bp_animes.get("/<int:anime_id>")
def filter():
    ...


@bp_animes.patch("/<int:anime_id>")
def update():
    ...


@bp_animes.delete("<int:anime_id>")
def delete():
    ...
