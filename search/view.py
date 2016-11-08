from flask import Blueprint, render_template

view = Blueprint('search', __name__, template_folder='templates', static_folder='static')

@view.route("/search")
def search_home():
    return "Here we implement search logic"
