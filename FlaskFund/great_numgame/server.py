from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'SecretKey'

guesses = 1
number = random.randint(1, 101)

while guesses > 0:
    guess = session['guess']

    guesses -= 1

@app.route('/')
def index():
    for i in range(1):
        number = random.randint(1,2)
        print random_num
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():

    return redirect('/')

app.run(debug=True)