#!/usr/bin/python3

from flask import Flask, redirect
from flask import Blueprint

app = Flask("CourierManagement", static_folder = None)

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

@app.route("/")
def redirector():
    return redirect("/home")

if __name__ == "__main__":
    app.secret_key = 'secret'
    app.run(debug=True)
