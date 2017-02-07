from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "thisissecret"

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/ninja')
def ninja():
    return render_template('/ninja.html')

@app.route('/ninja/<color>')
def color(color):
    return render_template('/color.html', color = color)

app.run(debug=True)
