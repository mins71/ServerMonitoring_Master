from flask import Blueprint, request, session, url_for, redirect, render_template

from models import models


test_ = Blueprint("test", __name__, url_prefix='/test')

@test_.route("/")
def index():
    return render_template("home/test.html")