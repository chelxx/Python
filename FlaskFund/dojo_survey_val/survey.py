from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGREX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask (__name__)
app.secret_key = 'SecretKeyBoii'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/maker', methods=['POST'])
def maker():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

@app.route('/result', methods=['POST'])
def ersult():
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
        return redirect('/')
    else:
        return render_template('result.html')

app.run(debug=True)