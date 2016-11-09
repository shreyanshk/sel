from flask import Blueprint, render_template, request, redirect
import sqlite3
view = Blueprint('track', __name__, template_folder='templates', static_folder='static')

@view.route('/track', methods = ['GET', 'POST'])
def track_home():
    if request.method == 'GET':
        return render_template('track.html')
    elif request.method == 'POST':
        return redirect('/track/' + request.form['cid'])

@view.route('/track/<cid>', methods = ['GET'])
def tracking_page(cid):
    def find_courier(courierid):
        conn = sqlite3.connect('couriers.sqlite')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("select * from couriers where cid = ?", [courierid])
        res = cursor.fetchall()
        return res
    details = find_courier(cid)
    result = ""
    for row in details:
    	for detail in row.keys():
            result += (detail + ": " + str(row[detail]))
            result += "<br>"
    if (len(result) == 0):
        return "No such courier in the system"
    else:
        return result

"""for row in res:
	for detail in row.keys():
		print(detail + ": " + str(row[detail]))
    print(" ")
"""
