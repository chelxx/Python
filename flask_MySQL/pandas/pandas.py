from flask import Flask, render_template, request, redirect, session
app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profview')
def view():
    return render_template('profview.html')

@app.route('/profedit')
def edit():
    return render_template('proedit.html')

@app.route('/profadd')
def edit():
    return render_template('add.html')

@app.route('/profadd', methods=['POST'])
def create():
    return render_template('add.html')

@app.route('/prof', methods=['POST'])
def update():
    return render_template('')

@app.route('/profview', methods=['POST'])
def delete():
    return