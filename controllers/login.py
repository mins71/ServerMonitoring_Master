from flask import Blueprint, request, session, url_for, redirect, render_template

from models import models


login_ = Blueprint("main", __name__, url_prefix='/')

@login_.route("/")
def index():
    if 'userid' in session:
        return f'Loggd in as {session["userid"]}. <a href="/logout">Logout</a><p></p><a href="/dashboard">gotodashboard</a>'
    else:
        return 'Not logged in. <a href=/login>Login</a>'


@login_.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        id = request.form['id']
        pw = request.form['pw']
        user = models
        row = user.SelectUser(id, pw)
        if row is not None:
            session['userid'] = row[0]
            session['username'] = row[1]
            return redirect(url_for('main.index'))
        else:
            return "Invalid id or pw!!!"
    return render_template("home/login.html")



@login_.route("/logout")
def logout():
    session.pop('userid', None)
    return redirect(url_for('main.index'))

