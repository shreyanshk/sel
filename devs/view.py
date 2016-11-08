from flask import Blueprint, render_template

view = Blueprint('devs', __name__, template_folder='templates', static_folder='static')

@view.route('/devs')
def developers():
    return "Made with <3 by Shreyansh & Vijay for VIT University"
