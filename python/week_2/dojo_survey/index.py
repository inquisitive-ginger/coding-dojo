from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    options = {
        'locations': ['San Jose', 'Seattle', 'San Fransisco'],
        'languages': ['Python', 'Javascript', 'C++', 'C']
    }

    return render_template('index.html', options=options)

@app.route('/result', methods=['POST'])
def result():
    results = {
        'name': request.form['user_name'],
        'location': request.form['dojo_location'],
        'language': request.form['fav_language'],
        'comments': request.form['comments']
    }

    return render_template('result.html', results=results)

app.run(debug=True)
