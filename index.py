#!/usr/bin/python3

from flask import Flask, url_for, render_template
import sqlite3

app = Flask("CourierManagement")

@app.route("/")
def welcome_page():
  return render_template('index.html')

@app.route('/add')
def add():
    return "this is where we ask the user to add new details"

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

@app.route('/update')
def update():
    return "This is where we ask the user for update details"

@app.route('/devs')
def developers():
    return "Made with <3 by Shreyansh & Vijay for VIT University"

@app.route("/search")
def search_home():
    return "Here we implement search logic"

conn = sqlite3.connect('couriers.sqlite')
cursor = conn.cursor()
cursor.execute("select * from couriers")
print(cursor.fetchall())
app.run(debug=True)
