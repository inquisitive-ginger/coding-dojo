from flask import Flask, request, render_template, redirect, session, flash
from mysqlconnection import MySQLConnector
from flask_wtf import Form
from flask_wtf.csrf import CsrfProtect
from wtforms import StringField, validators

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this_is_a_secret'

mysql = MySQLConnector(app, 'cd_test')

class EmailForm(Form):
    email = StringField('E-mail Address', [validators.DataRequired(message='This field is required.'),
                                           validators.Email(message='Please enter a valid address.')])
def add_email(user_email):
    query = 'INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())'
    data = {
        'email': user_email
    }
    mysql.query_db(query, data)

    return redirect('/')

@app.route('/delete/<id>')
def delete_email(id):
    query = 'DELETE FROM emails WHERE id = :id'
    data = {
        'id': id
    }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = EmailForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            return add_email(request.form['email'])
        else:
            print form.errors

    # get e-mails to display
    query = 'SELECT * FROM emails'
    emails = mysql.query_db(query)

    return render_template('index.html', form=form, emails=emails)

app.run(debug=True)
