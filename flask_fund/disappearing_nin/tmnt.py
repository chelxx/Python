from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    pizzaparty=True
    return render_template('ninja.html', pizzaparty=pizzaparty)

@app.route('/ninja/<color>')
def colors(color):
    pizzaparty = False
    return render_template('ninja.html', color=color, pizzaparty=pizzaparty)


app.run(debug=True)