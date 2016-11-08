from flask import Blueprint, render_template

view = Blueprint('update', __name__, template_folder='templates', static_folder='static')

@view.route('/update')
def update():
    return "This is where we ask the user for update details"
