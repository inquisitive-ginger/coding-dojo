from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'tis_a_secret'

@app.route('/')
def home():
    if 'name' not in session:
        session['name'] = ''
    if 'lang' not in session:
        session['lang'] = ''
    if 'loc' not in session:
        session['loc'] = ''
    if 'comment' not in session:
        session['comment'] = ''
    if 'error_state' not in session:
        session['error_state'] = 'hidden'

    languages = ['Javascript', 'Python', 'C/C++', 'Java', 'PHP']
    locations = ['Bellevue', 'San Jose', 'Los Angeles', 'Dallas', 'Washington DC', 'Chicago']
    return render_template('index.html', languages=languages, locations=locations)

@app.route('/result', methods=['POST'])
def validate():
    errors = 0
    if len(request.form['name']) < 1:
        errors += 1
        flash("Name cannot be empty.")
    if len(request.form['comment']) < 1:
        errors += 1
        flash("Comment cannot be empty.")
    if len(request.form['comment']) > 120:
        errors += 1
        flash("Comment cannot be greater than 120 characters.")

    if errors > 0:
        session['error_state'] = 'visible'
        session['redirect'] = True
        return redirect('/')
    else:
        session['error_state'] = 'hidden'
        session['redirect'] = False
        session['name'] = request.form['name']
        session['lang'] = request.form['language']
        session['loc'] = request.form['location']
        session['comment'] = request.form['comment']

    return render_template('result.html')


app.run(debug=True)
