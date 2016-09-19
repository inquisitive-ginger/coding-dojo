from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def hello_world():
    if (session.get('visits') is not None and
        session.get('redirect') is not True):
        session['visits'] += 1
        session['redirect'] = False

    return render_template('index.html')

@app.route('/add-two', methods=["POST"])
def addTwo():
    session['visits'] += 2
    session['redirect'] = True
    return redirect('/')

@app.route('/reset', methods=["POST"])
def reset():
    session['visits'] = 0
    session['redirect'] = True
    return redirect('/')

app.run(debug=True)
