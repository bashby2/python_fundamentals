from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re

app = Flask(__name__)
app.secret_key = "someThing_Verysecret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# For validating the email address
mysql = MySQLConnector(app,'wall_db')
bcrypt = Bcrypt(app)
# For encrypting passwords

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    errors = False
    if len(request.form['first_name']) < 2:
        flash('First name must be at least 2 characters')
        errors = True
    if len(request.form['last_name']) < 2:
        flash('Last name must be at least 2 characters')
        errors = True
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email')
        errors = True
    if len(request.form['password']) < 8:
        flash('Password must be at least 8 characters')
        errors = True
    elif request.form['password'] != request.form['confirm']:
        flash('Passwords must match')
        errors = True
    if errors == False:
        hashed_pw = bcrypt.generate_password_hash(request.form['password'])
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': hashed_pw
        }
        user_id = mysql.query_db(query, data)
        session['user_id'] = user_id
        return render_template('wall.html', first_name=user[0]['first_name'])
    else:
        return redirect('/')

@app.route('/login', methods=["POST"])
def login():
    errors = False
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email')
        errors = True
    if len(request.form['password']) < 8:
        flash('Password must be at least 8 characters')
        errors = True
    if errors:
        return redirect('/')
    else:
        query = "SELECT * FROM users WHERE email = :email"
        data = {
            'email': request.form['email']
        }
        user = mysql.query_db(query, data)
        if user and bcrypt.check_password_hash(user[0]['password'], request.form['password']):
            session['user_id'] = user[0]['id']
            return render_template('wall.html', first_name=user[0]['first_name'], user=session['user'])
        else:
            flash('Email/Password not found')
            return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')

app.run(debug=True)
