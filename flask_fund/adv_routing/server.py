from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print username
    print id
    return render_template("user.html", username = username, id = id)

@app.route('/route/with/<vararg>')
def handler_function(vararg):
    print vararg

app.run(debug=True)