from flask import Flask, render_template, redirect, request, session
import random, time, datetime

app = Flask(__name__)
app.secret_key = 'this_is_a_secret'

@app.route('/')
def home():
    if 'gold' not in session:
        session['gold'] = 0
    if 'activities' not in session:
        session['activities'] = []

    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    results = {
        'farm': random.randint(10,20),
        'casino': random.randint(-50, 50),
        'house': random.randint(2,5),
        'cave': random.randint(5,10)
    }

    destination_explored = request.form['destination']
    gold_earned = results[destination_explored]
    session['gold'] += gold_earned

    ts = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    log = "You explored a {} and {} {} gold. [{}] ".format(destination_explored,
                                                           ('lost','earned')[gold_earned > 0],
                                                           abs(gold_earned),
                                                           ts)

    session['activities'].insert(0, log)

    return redirect('/')

app.run(debug=True)
