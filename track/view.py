from flask import Blueprint, render_template, request, redirect
import sqlite3
view = Blueprint('track', __name__, template_folder='templates', static_folder='static')

@view.route('/track', methods = ['GET', 'POST'])
def track_home():
    if request.method == 'GET':
        return render_template('track.html')
    elif request.method == 'POST':
        return redirect('/track/' + request.form['cid'])

@view.route('/track/<cid>')
def tracking_page(cid):
    def find_courier(cid):
        conn = sqlite3.connect('couriers.sqlite')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("select * from couriers where cid = ?", cid)
        res = cursor.fetchone()
        return res
    details = find_courier(cid)
    result = []
    for detail in details.keys():
        value = details[detail]
        result.append(detail + ": " + str(value) + "<br>")
    return result
