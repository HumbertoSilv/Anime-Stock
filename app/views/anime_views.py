from flask import Blueprint

bp_animes = Blueprint("anime_bp", __name__, url_prefix="/anime")


@bp_animes.route(" ", methods=("GET", "POST"))
def get_create():
    ...


@bp_animes.get("/<int:anime_id>")
def filter():
    ...


@bp_animes.patch("/<int:anime_id>")
def update():
    ...


@bp_animes.delete("<int:anime_id>")
def delete():
    ...
