from flask import Blueprint, request, session, url_for, redirect, render_template

from models import pclist
from service.issue_data import call_issue

pcstatue_ = Blueprint("statue", __name__, url_prefix='/slavelist')


@pcstatue_.route("/")
def main():
    if 'userid' not in session:
        return redirect(url_for("main.index"))
    data = pclist.CellPc()
    return render_template("home/tables.html", segment='pc', data=data)

@pcstatue_.route("/<pcname>")
def index(pcname):
    if 'userid' not in session:
        return redirect(url_for("main.index"))
    pc = pclist.cell_pc_name()
    if pcname in pc:
        issue = call_issue(list(pcname.split()))
        return render_template("home/pcstatue.html", segment='pc', select_segment=pcname, data=pcname, issue = issue)
    else:
        return '404'