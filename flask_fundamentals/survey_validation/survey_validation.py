from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "thisissecret"

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    if len(request.form['name']) < 1:
        flash("Please enter your name.")
        return render_template("index.html")
    elif len(request.form['comment']) > 120:
        flash("Please keep your comments under 120 characters.")
        return render_template("index.html")
    else:
        print "Got Post Info"
        print request.form
        form_results = {
            'name': request.form['name'],
            'location': request.form['location'],
            'language': request.form['language'],
            'comment': request.form['comment']
        }
        return render_template("redirect_page.html", results=form_results)
app.run(debug=True) # run our server
