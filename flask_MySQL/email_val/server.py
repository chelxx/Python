from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'SecretKey'
mysql = MySQLConnector(app,'email_val')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
    query = "SELECT * FROM emails WHERE address = :address"
    data = {
        'address': request.form['address']
    }
    mails = mysql.query_db(query, data)
    if mails:
        query = "SELECT * FROM emails"
        allmail = mysql.query_db(query, data)
        return render_template('success.html', allmail = allmail)
    else:
        flash ('Email is not in the database!')
        return redirect('/')

app.run(debug=True)