from flask import Blueprint, render_template, url_for

view = Blueprint('home',
    __name__,
    template_folder = 'templates',
    static_folder = 'static'
    )

@view.route("/home")
def welcome_page():
    return render_template('index.html')
