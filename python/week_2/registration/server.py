from flask import Flask, session, request, render_template, redirect
import re

app = Flask(__name__)
app.secret_key = 'tis_a_secret'

@app.route('/')
def home(form_errors=None):
    print form_errors
    return render_template('index.html', form_errors=form_errors)

@app.route('/validate', methods=['POST'])
def validate():
    form_errors = {}
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

    # name validation
    if len(request.form['first_name']) < 1:
        form_errors['f_name'] = {
            'valid': False,
            'message': 'Please enter your first name.'
        }
    if len(request.form['last_name']) < 1:
        form_errors['l_name'] = {
            'valid': False,
            'message': 'Please enter your last name.'
        }

    # email validation
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    email_match = re.search(email_regex, request.form['email'])
    if len(request.form['email']) < 1:
        form_errors['email'] = {
            'valid': False,
            'message': 'Please enter your e-mail address.'
        }
    elif not email_match:
        form_errors['email'] = {
            'valid': False,
            'message': 'Please enter a valid e-mail address.'
        }

    # password validation
    pass_regex = r"([A-Z0-9]+)"
    pass_match = re.search(pass_regex, request.form['password'])
    if len(request.form['password']) < 8 or not pass_match:
        form_errors['pass'] = {
            'valid': False,
            'message': 'Password must be at least 8 characters, including 1 uppercase letter and 1 number.'
        }
    elif request.form['password'] != request.form['confirm_password']:
        form_errors['pass'] = {
            'valid': False,
            'message': 'Passwords do not match.'
        }

    if len(request.form['confirm_password']) < 1:
        form_errors['c_pass'] = {
            'valid': False,
            'message': 'Please confirm your password'
        }

    #make sure e-mail is valid
    if len(request.form['last_name']) < 1:
        form_errors['l_name'] = {
            'valid': False,
            'message': 'Please enter a last name.'
        }

    if form_errors != {}:
        return home(form_errors)

    return render_template('result.html')

app.run(debug=True)
