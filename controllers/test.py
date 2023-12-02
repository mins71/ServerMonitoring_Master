from flask import Blueprint, request, session, url_for, redirect, render_template

from models import pclist


test_ = Blueprint("test", __name__, url_prefix='/test')

@test_.route("/")
def index():
    return render_template("home/get.html")

@test_.route("/get")
def get_():
    return "test sniff"