from flask import Blueprint, request, session, url_for, redirect, render_template


managment_ = Blueprint("managment", __name__, url_prefix='/mgmt')

@managment_.route('/')
def index():
    if 'userid' in session and '1' in session['level']:
        return "redirect(url_for(''))"
        