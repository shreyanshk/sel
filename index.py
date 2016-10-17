from flask import Flask, url_for, render_template

app = Flask("CourierManagement")

@app.route("/")
def welcome_page():
  return render_template('index.html')

@app.route('/track')
def track_home():
    return "this is where we ask user for courier id"

@app.route('/track/<courierid>')
def tracking_page(courierid):
    def find_courier(courierid):
        #sql logic here, put result in result variable
        return "this is where we track courier with id " + courierid
    result = find_courier(courierid)
    return result

@app.route('/devs')
def developers():
    return "Made with <3 by Shreyansh & Vijay for VIT University"

@app.route("/search")
def search_home():
    return "Here we implement search logic"

app.run()
