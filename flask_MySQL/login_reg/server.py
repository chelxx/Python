from flask import Flask, request, redirect, render_template, session, flash #import
from mysqlconnection import MySQLConnector #bridge
import md5, os, binascii, re #for (1)hashing, (2)salt, (1)regex
EMAIL_REGREX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGREX = re.compile(r'^[a-zA-Z0-9.+_-]+$')
app = Flask(__name__)
app.secret_key = 'SecretKey'
mysql = MySQLConnector(app,'logregdb') #database connection

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST']) #route for registering a user
def register():
    error = []

    if not EMAIL_REGREX.match(request.form['email']):
        error.append ('Invalid Email Address!')
    if not NAME_REGREX.match(request.form['first_name']):
        error.append ('Invalid First Name!')
    if not NAME_REGREX.match(request.form['last_name']):
        error.append ('Invalid Last Name!')
    if request.form['confirm_password'] != request.form['password']:
        error.append ('Try again! Invalid Password Input!')
    if len(error) == 0:
        pw = request.form['password'] 
        salt = binascii.b2a_hex(os.urandom(15))
        hs_password = md5.new(pw + salt).hexdigest()
        query = "INSERT INTO users (first_name, last_name, email, hs_password, created_at, updated_at, salt) VALUES (:first_name, :last_name, :email, :hs_password, NOW(), NOW(), :salt)"
        data = {
            'first_name': request.form['first_name'],
            'last_name':  request.form['last_name'],
            'email': request.form['email'],
            'hs_password': hs_password,
            'salt': salt
            }    
        mysql.query_db(query, data)
    for i in error:
        flash(i)
    return redirect('/')

@app.route('/success', methods=['POST']) #route for loggin in a user
def success():
    logerror = [] #error container
    query = "SELECT * FROM users WHERE email = :email" #query for SQL
    mail = {'email': request.form['logemail']} #input for database, works with code
    login = mysql.query_db(query, mail) #works with mail
    if not login: #if email is not in the db
        logerror.append('Invalid Email!')
    else: # if email is there
        temppass = request.form['logpassword']
        salt = login[0]['salt']
        pswd = md5.new(temppass + salt).hexdigest() 
        if not pswd == login[0]['hs_password']:
            logerror.append('Invalid Password!')
        if len(logerror) == 0:
            return render_template('success.html', email=login[0]['email']) #for sending into html
    for i in logerror:
        flash(i)
    return redirect('/')

app.run(debug=True)