import flask
from flask import Blueprint, redirect, url_for
from flask import current_app as current_app

first_set_bp = Blueprint(
    "first_set_bp", __name__,
    template_folder='templates',
    static_folder='static'
)

# 1_4 graphs

@first_set_bp.route("/BC1/")
def BC1():
    return flask.render_template("1_4_pre.html")

@first_set_bp.route("/BC1/m/")
def m():
    return flask.render_template("f_mask_1.html")

@first_set_bp.route("/BC1/m/BG1/")
def BG1():
    return flask.render_template("1_4_po.html")

@first_set_bp.route("/BC1/m/BG1/bt1")
def bt1():
    return flask.render_template("f_btwnqs_1.html")

 # 1_8 graphs

@first_set_bp.route("/BC1/m/BG1/bt1/BC2")
def BC2():
    return flask.render_template("1_8_pre.html")

@first_set_bp.route("/BC1/m/BG1/bt1/BC2/m2")
def m2():
    return flask.render_template("f_mask_2.html")

@first_set_bp.route("/BC1/m/BG1/bt1/BC2/m2/BG2")
def BG2():
    return flask.render_template("1_8_po.html")

@first_set_bp.route("/BC1/m/BG1/bt1/BC2/m2/BG2/bt2")
def bt2():
    return flask.render_template("f_btwnqs_2.html")

# 2_4 graphs

@first_set_bp.route("/BC1/m/BG1/bt1/BC2/m2/BG2/bt2/BC3")
def BC3():
    return flask.render_template("2_4_pre.html")

@first_set_bp.route("/BC1/m/BG1/bt1/BC2/m2/BG2/bt2/BC3/m3")
def m3():
    return flask.render_template("f_mask_3.html")

@first_set_bp.route("/BC1/m/BG1/bt1/BC2/m2/BG2/bt2/BC3/m3/BG3")
def BG3():
    return flask.render_template("2_4_po.html")