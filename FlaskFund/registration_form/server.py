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
    if len(request.form['first_name']) < 1:
        flash ('First name cannot be blank!')
    if len(request.form['last_name']) < 1:
        flash ('Last name cannot be blank!')
    if len(request.form['password']) < 1:
        flash ('Password cannot be blank!')
    if request.form['confirm_password'] != request.form['password']:
        flash ('Passwords do not match!')
    return redirect('/')

app.run(debug=True)