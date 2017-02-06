from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NUMBER_REGEX = re.compile(r'.*[0-9]+')
LETTER_REGEX = re.compile(r'.*[a-zA-Z]+')
UPPER_REGEX = re.compile(r'.*[A-Z]+')
app = Flask(__name__)
app.secret_key = "thisissecret"

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    if len(request.form['email']) < 1:
        flash("Please enter your email.")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Please enter a valid email.")
    elif len(request.form['first_name']) < 1:
        flash("Please enter your first name.")
    elif len(request.form['last_name']) < 1:
        flash("Please enter your last name.")
    elif len(request.form['password']) < 9:
        flash("Please enter your password. Your password must be at least 8 charaters")
    elif not LETTER_REGEX.match(request.form['password']):
        flash("Your password must contain at least one letter")
    elif not UPPER_REGEX.match(request.form['password']):
        flash("Your password must contain at least one upper case letter.")
    elif not NUMBER_REGEX.match(request.form['password']):
        flash("Your password must contain at least one number")
    elif request.form['confirm_password'] != request.form['password']:
        flash("Your passwords do not match. Please enter your password.")
    else:
        flash("Thank you for submitting your form.")
    return redirect('/')
app.run(debug=True) # run our server
