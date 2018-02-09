from flask import Flask, render_template
app = Flask(__name__)

@app.route('/world')
def hello_world():
    return render_template('index.html')

app.run(debug=True)