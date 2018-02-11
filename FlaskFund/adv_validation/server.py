from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGREX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'SecretKey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
        flash ('Email cannot be blank!')
    elif not EMAIL_REGREX.match(request.form['email']):
        flash ('Invalid Email Address!')
    else:
        flash ('Success!')
    return redirect('/')

app.run(debug=True)