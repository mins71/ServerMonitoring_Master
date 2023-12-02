from flask import Blueprint, render_template, request, session, url_for, redirect

from models import pclist
from service.issue_data import call_issue

dashboard_ = Blueprint("dashboard", __name__, url_prefix='/dashboard')

@dashboard_.route("/")
def index():
    if 'userid' not in session:
        return redirect(url_for("main.index"))
    data = pclist.CellPc()
    issue = call_issue()
    return render_template("home/dashboard.html", segment='dashboard', data=data, issue = issue)