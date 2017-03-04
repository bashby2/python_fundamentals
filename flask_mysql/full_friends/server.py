from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'users')

@app.route('/')
def index():
    query = "SELECT * FROM users" # define your query
    users = mysql.query_db(query) # run query with query_db()
    return render_template('index.html', all_users=users) # pass data to our template

@app.route('/users', methods=['POST'])
def create():
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'email': request.form['email']
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/users/<user_id>')
def show(user_id):
    # Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.
    query = "SELECT * FROM users WHERE id = :specific_id"
    # Then define a dictionary with key that matches :variable_name in query.
    data = {'specific_id': user_id}
    # Run query with inserted data.
    users = mysql.query_db(query, data)
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.
    return render_template('index.html', one_user=users[0])

@app.route('/update_user/<user_id>', methods=['POST'])
def update(user_id):
    query = "UPDATE users SET first_name = :first_name, last_name = :last_name, email = :email, WHERE id = :id"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'email': request.form['email'],
             'id': user_id
           }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/users/<user_id>', methods=['POST'])
def delete(user_id):
    query = "DELETE FROM users WHERE id = :id"
    data = {'id': user_id}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
