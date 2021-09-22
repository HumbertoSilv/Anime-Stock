from flask import Blueprint, request
from app.services.anime_services import Animes
# from app.exc.exc import InvalidKeys

bp_animes = Blueprint("anime_bp", __name__, url_prefix="/animes")


@bp_animes.route("", methods=["GET", "POST"])
def get_create():
    if request.method == "POST":
        try:
            data = request.json
            anime = Animes(**data)
            return {"msg": anime.__dict__}

        except TypeError as e:
            return {"available_key": ["anime", "released_date", "seasons"],
                    "wrong_keys_sended": [str(e).split("'")[1]]}


@bp_animes.get("/<int:anime_id>")
def filter():
    ...


@bp_animes.patch("/<int:anime_id>")
def update():
    ...


@bp_animes.delete("<int:anime_id>")
def delete():
    ...
