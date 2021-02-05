import flask
from flask import Blueprint
from flask import current_app as current_app

training_bp = Blueprint(
    "training_bp", __name__,
    template_folder='templates',
    static_folder='static'
)

@training_bp.route("/game")
def game():
    return flask.render_template("game.html")

@training_bp.route("/game/BC")
def BC():
    return flask.render_template("BC.html")

@training_bp.route("/game/BC/m")
def trm():
    return flask.render_template("trmask.html")

@training_bp.route("/game/BC/m/BG")
def BG():
    return flask.render_template("BG.html")

@training_bp.route("/game/BC/m/BG/trans")
def trans():
    return flask.render_template("trans.html")