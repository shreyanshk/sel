from flask import Blueprint, render_template, request
import sqlite3
from flask_wtf import Form
from wtforms import StringField, DecimalField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField

view = Blueprint('add', __name__, template_folder='templates', static_folder='static')

class CourierDetails(Form):
    cid = StringField('Courier ID', validators=[DataRequired()])
    sender = StringField('Sender Name')
    saddr = StringField('Sender Address')
    receiver = StringField('Receiver Name')
    raddr = StringField('Receiver Address')
    rcell = IntegerField('Receiver Contact')
    status = StringField('Current Status')
    scell = IntegerField('Sender Contact')
    wt = DecimalField('Weight')
    length = IntegerField('Length')
    height = IntegerField('Height')
    breath = IntegerField('Breath')
    idmarks = TextAreaField('Identification Marks')
    date = DateField('Date Received', format = '%y-%m-%d')
    submit = SubmitField('Submit')



@view.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        form = CourierDetails()
        return render_template('add.html', form = form)
    elif request.method == 'POST':
        form = CourierDetails(request.form)
        if True:
            conn = sqlite3.connect('./couriers.sqlite')
            cursor = conn.cursor()
            query = "insert into couriers values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            values = ([form.cid.data], [form.sender.data], [form.saddr.data], [form.scell.data], [form.receiver.data], [form.raddr.data], [form.rcell.data], [form.wt.data], [form.length.data], [form.breath.data], [form.height.data], [form.idmarks.data], [form.status.data], [form.date.data])
            cursor.execute(query, (form.cid.data, form.sender.data, form.saddr.data, form.scell.data, form.receiver.data, form.raddr.data, form.rcell.data, form.wt.data, form.length.data, form.breath.data, form.height.data, form.idmarks.data, form.status.data, str([form.date.data]), ))
            conn.commit()
            conn.close()
            return "Entry Added!"
        else:
            return "Error!"
            return render_template('add_error.html', form = form)
