import flask
from flask import Blueprint
from flask import current_app as current_app
from flask import redirect, url_for, session, app
from datetime import timedelta

SpAb_bp = Blueprint(
    "SpAb_bp", __name__, 
    template_folder='templates',
    static_folder='static'
)

@SpAb_bp.before_request
def make_session_permanent():   
    session.permanent = True
    SpAb_bp.permanent_session_lifetime=timedelta(minutes=3)
    session.modified = True


@SpAb_bp.route("/instrctn")
def instrctn():
    return flask.render_template("instruction.html")

@SpAb_bp.route("/Qs")
def Qs():
    return flask.render_template("Qs.html")

@SpAb_bp.route("/Qs/done")
def done():
    return redirect(url_for("quest"))

