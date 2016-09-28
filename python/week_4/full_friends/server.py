from flask import Flask, request, render_template, redirect, session, flash
from mysqlconnection import MySQLConnector
from flask_wtf import Form
from wtforms import StringField, validators

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this_is_a_secret'

mysql = MySQLConnector(app, 'cd_test')

class FriendForm(Form):
    first_name = StringField('First Name', [validators.DataRequired(message='This field is required.')])
    last_name = StringField('Last Name', [validators.DataRequired(message='This field is required.')])
    email = StringField('E-mail Address', [validators.DataRequired(message='This field is required.'),
                                           validators.Email(message='Please enter a valid e-mail.')])


@app.route('/')
def index():
    add_friend_form = FriendForm()

    query = 'SELECT * FROM users'
    users = mysql.query_db(query)

    return render_template('index.html', form=add_friend_form, friends=users)

@app.route('/friends', methods=['POST'])
def create():
    add_friend_form = FriendForm(request.form)
    if add_friend_form.validate_on_submit():
        query = """
                    INSERT INTO users (first_name, last_name, email, created_at, updated_at)
                    VALUES(:first_name, :last_name, :email, NOW(), NOW())
                """

        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email']
        }

        mysql.query_db(query, data)
        return redirect('/')
    else:
        query = 'SELECT * FROM users'
        users = mysql.query_db(query)
        return render_template('index.html', form=add_friend_form, friends=users)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
    # check that form validates
    update_friend_form = FriendForm(request.form)

    if update_friend_form.validate_on_submit():
        query = """
                    UPDATE users SET first_name = :fname, last_name = :lname, email = :email, updated_at = NOW()
                    WHERE id = :id
                """
        data = {
            'fname': request.form['first_name'],
            'lname': request.form['last_name'],
            'email': request.form['email'],
            'id': id
        }
        mysql.query_db(query, data)
        return redirect('/')

    return render_template('edit-user.html', form=update_friend_form, user_id=id)

@app.route('/friends/<id>/edit')
def edit(id):
    # get friend information from DB
    query = 'SELECT * FROM users WHERE id = :id'
    data = {'id': id}
    friend = mysql.query_db(query, data)[0]

    # create form for update and pre-populate with DB data
    update_friend_form = FriendForm()
    update_friend_form.first_name.data = friend['first_name']
    update_friend_form.last_name.data = friend['last_name']
    update_friend_form.email.data = friend['email']

    return render_template('edit-user.html', form=update_friend_form, user_id=id)

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    query = 'DELETE FROM users WHERE id=:id'
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
