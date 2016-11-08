from flask import Blueprint, render_template
import sqlite3
view = Blueprint('track', __name__, template_folder='templates', static_folder='static')

@view.route('/track')
def track_home():
    conn = sqlite3.connect('couriers.sqlite')
    cursor = conn.cursor()
    return "this is where we ask user for courier id"

@view.route('/track/<courierid>')
def tracking_page(courierid):
    def find_courier(courierid):
        #sql logic here, put result in result variable
        return "this is where we track courier with id " + courierid
    result = find_courier(courierid)
    return result
