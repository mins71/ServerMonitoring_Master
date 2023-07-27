from flask import Blueprint, render_template, request, session, url_for, redirect

from models import models
dashboard_ = Blueprint("dashboard", __name__, url_prefix='/dashboard')

@dashboard_.route("/")
def index():
    if 'userid' not in session:
        return redirect(url_for("main.index"))
    return render_template("home/dashboard.html", segment='dashboard')