from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos/new', methods=['POST'])
def dojos():
    print "Got Post Info"
    name = request.form['name']
    email = request.form['email']
    request.form['name']CXZert
    request.form['email']
    print request.form
    return render_template('dojos.html')

app.run(debug=True)