from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ninja')
def ninjas():
    ninjas = ['donatello', 'leonardo', 'michelangelo', 'raphael']
    return render_template('ninja.html', ninjas=ninjas)

@app.route('/ninja/<color>')
def ninja(color):
    ninja = []
    if color == 'blue':
        ninja.append('leonardo')
    elif color == 'orange':
        ninja.append('michelangelo')
    elif color == 'red':
        ninja.append('raphael')
    elif color == 'purple':
        ninja.append('donatello')
    else:
        ninja.append('notapril')

    return render_template('ninja.html', ninjas=ninja)

app.run(debug=True)
