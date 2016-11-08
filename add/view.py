from flask import Blueprint, render_template

view = Blueprint('add', __name__, template_folder='templates', static_folder='static')

@view.route('/add')
def add():
    return "this is where we ask the user to add new details"
