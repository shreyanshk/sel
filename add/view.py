from flask import Blueprint, render_template, request
import sqlite3
from wtforms import Form, StringField, validators


view = Blueprint('add', __name__, template_folder='templates', static_folder='static')

@view.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.html')
    elif request.method == 'POST':
        form = request.form
        conn = sqlite3.connect('./couriers.sqlite')
        cursor = conn.cursor()
        query = "insert into couriers values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, form);
        return "Entry Added!"
