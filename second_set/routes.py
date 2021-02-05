import flask
from flask import Blueprint
from flask import current_app as current_app
from flask import redirect, url_for

second_set_bp = Blueprint(
    "second_set_bp", __name__,
    template_folder='templates',
    static_folder='static'
)

#  2_8 graphs

@second_set_bp.route("/btwnqs")
def btwnqs():
    return flask.render_template("s_btwnqs_1.html")

@second_set_bp.route("/BC1/")
def BC1():
    return flask.render_template("2_8_pre.html")

@second_set_bp.route("/BC1/m/")
def m():
    return flask.render_template("s_mask_1.html")

@second_set_bp.route("/BC1/m/BG1/")
def BG1():
    return flask.render_template("2_8_po.html")

@second_set_bp.route("/BC1/m/BG1/bt1")
def bt1():
    return flask.render_template("s_btwnqs_2.html")

 # 1_16 graphs

@second_set_bp.route("/BC1/m/BG1/bt1/BC2")
def BC2():
    return flask.render_template("1_16_pre.html")

@second_set_bp.route("/BC1/m/BG1/bt1/BC2/m2")
def m2():
    return flask.render_template("s_mask_2.html")

@second_set_bp.route("/BC1/m/BG1/bt1/BC2/m2/BG2")
def BG2():
    return flask.render_template("1_16_po.html")

@second_set_bp.route("/BC1/m/BG1/bt1/BC2/m2/BG2/bt2")
def bt2():
    return flask.render_template("s_btwnqs_3.html")

# 3_4 graphs

@second_set_bp.route("/BC1/m/BG1/bt1/BC2/m2/BG2/bt2/BC3")
def BC3():
    return flask.render_template("3_4_pre.html")

@second_set_bp.route("/BC1/m/BG1/bt1/BC2/m2/BG2/bt2/BC3/m3")
def m3():
    return flask.render_template("s_mask_3.html")

@second_set_bp.route("/BC1/m/BG1/bt1/BC2/m2/BG2/bt2/BC3/m3/BG3")
def BG3():
    return flask.render_template("3_4_po.html")