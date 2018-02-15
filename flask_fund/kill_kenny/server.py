from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'SecretKey'

@app.route('/')
def index():
    if not 'deaths' in session:
        session['deaths'] = 0
    
    return render_template('home.html', deaths=session['deaths'])

@app.route('/yes_dead')
def yes_dead():
    session['deaths'] += 1
    return render_template('yes_dead.html')

@app.route('/no_live')
def no_live():
    return render_template('no_live.html')

@app.route('/no_tv')
def no_tv():
    return render_template('no_tv.html')

@app.route('/yes_tv')
def yes_tv():
    session['deaths'] += 1
    return render_template('yes_tv.html')

@app.route('/no')
def no():
    return render_template('no.html')

@app.route('/yes')
def yes():
    session['deaths'] += 1
    return render_template('yes.html')

@app.route('/restart', methods=['POST'])
def ninja2():
    if request.form['restart']:
        session['deaths'] = 0
    return redirect('/')

app.run(debug=True)