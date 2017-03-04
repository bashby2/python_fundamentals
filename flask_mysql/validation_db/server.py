from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


app = Flask(__name__)
app.secret_key = "thisissecret"
mysql = MySQLConnector(app,'usersdb')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def create_user():
    if len(request.form['email']) < 1:
        flash("Please enter your email.")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Please enter a valid email.")
    else:
        session['email'] = request.form['email']
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {
             'email': session['email']
        }
        mysql.query_db(query, data)
        return render_template('/success.html')
    return redirect('/')

@app.route('/success')
def query():
    query = "SELECT * FROM emails"# define your query
    emails = mysql.query_db(query)# run query with query_db()
    return render_template('success.html', email_dict=emails, email_submitted=session['email'])

app.run(debug=True)
