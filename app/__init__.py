from flask import Flask
from app.views import anime_views


def create_app():
    app = Flask(__name__)
    app.register_blueprint(anime_views.bp_animes)
    return app
