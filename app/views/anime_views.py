from flask import Blueprint, request
from app.services.anime_services import Animes
from psycopg2.errors import UniqueViolation
from app.exc.exc import AnimeNotFound


bp_animes = Blueprint("anime_bp", __name__, url_prefix="/animes")


@bp_animes.route("", methods=["GET", "POST"])
def get_create():
    if request.method == "POST":
        try:
            data = request.json
            anime = Animes(**data)
            saved = anime.save()
            return saved, 201

        except TypeError as e:
            return {"available_key": ["anime", "released_date", "seasons"],
                    "wrong_keys_sended": [str(e).split("'")[1]]
                    }, 422

        except UniqueViolation:
            return {"error": "anime already exists."}, 409

    return Animes.get_all(), 200


@bp_animes.get("/<int:anime_id>")
def filter(anime_id: int):
    try:
        anime = Animes.get_by_id(anime_id)
        return anime, 200

    except AnimeNotFound:
        return {"error": "Not found."}, 404


@bp_animes.patch("/<int:anime_id>")
def update():
    ...


@bp_animes.delete("<int:anime_id>")
def delete():
    ...
