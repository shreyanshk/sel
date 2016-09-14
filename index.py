from flask import Flask
app = Flask("CourierManagement")

@app.route("/")
def hello_world():
  return "Welcome to VIT's courier Management System"

@app.route('/track')
def track_home():
    return "this is where we ask user for courier id"

@app.route('/track/<courierid>')
def tacking_page(courierid):
    return "this is where we track courier with id " + courierid

@app.route('/devs')
def developers():
    return "Made with <3 by Shreyansh & Vijay for VIT University"

app.run()
