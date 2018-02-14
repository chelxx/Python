from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'SecretKey'

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] += 1
    return render_template('index.html', counter=session['counter'])

@app.route('/plustwo', methods=['POST'])
def ninja1():
    session['counter'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def ninja2():
    if session['counter'] > 0:
        session['counter'] = 0
    return redirect('/')

app.run(debug=True)