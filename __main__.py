#!/usr/bin/python3

from flask import Flask, url_for, render_template
from flask import Blueprint

app = Flask("CourierManagement")

from home.view import view as homeview
app.register_blueprint(homeview)

from search.view import view as searchview
app.register_blueprint(searchview)

from track.view import view as trackview
app.register_blueprint(trackview)

from add.view import view as addview
app.register_blueprint(addview)

from update.view import view as updateview
app.register_blueprint(updateview)

from devs.view import view as devsview
app.register_blueprint(devsview)

if __name__ == "__main__":
    app.run(debug=True)
