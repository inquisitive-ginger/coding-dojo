from flask import Flask, render_template, request, redirect, session, url_for
import random

app = Flask(__name__)
app.secret_key = 'to_know_a_secret'


@app.route('/', methods=['GET', 'POST'])
def home():
    classes = {}
    result = ''

    # new game started
    if (session.get('number') is None):
        session['number'] = random.randrange(0, 101)
        result = 'You haven\'t guessed yet. Hop to it.'
        classes = {
            'result-state': 'no-guess',
            'result-display': 'hidden',
            'pa-display': 'hidden'
        }
    # # current game exists, evaluate guess
    elif ('guess' in request.form):
        guess = int(request.form['guess'])
        if (guess == session.get('number')):
            result = 'You got it! Good work.'
            classes = {
                'result-state': 'correct',
                'result-display': 'visible',
                'pa-display': 'visible'
            }
        elif (guess > session.get('number')):
            result = 'Too high mate. Guess again.'
            classes = {
                'result-state': 'too-high',
                'result-display': 'visible',
                'pa-display': 'hidden'
            }
        else:
            result = 'Too low mate. Guess again.'
            classes = {
                'result-state': 'too-low',
                'result-display': 'visible',
                'pa-display': 'hidden'
            }
    else:
        return 'Something went wrong. Sorry \'bout that. Clear your cache and refresh?'

    return render_template('index.html', classes=classes, result=result)

@app.route('/reset')
def reset():
    session.pop('number')
    return redirect('/')

app.run(debug=True)
