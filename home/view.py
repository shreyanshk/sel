from flask import Blueprint, render_template

view = Blueprint('home', __name__, template_folder='templates', static_folder='static')

@view.route("/")
def welcome_page():
  return render_template('index.html')
