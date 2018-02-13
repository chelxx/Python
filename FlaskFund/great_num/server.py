from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'SecretKey'

@app.route('/')
def index():
    if 'num' not in session:
        session['num'] = random.randint(1, 101)
    else:
        pass
    print session['num']
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    if int(request.form['guess']) < session['num']:
        session['message'] = 'TOO LOW!'
    elif int(request.form['guess']) > session['num']:
        session['message'] = 'TOO HIGH!'
    elif int(request.form['guess']) == session['num']:
        session['message'] = 'YOU GOT IT!'
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    if session['num'] > 0:
        session['num'] = random.randint(1, 101)
    return redirect('/')

app.run(debug=True)