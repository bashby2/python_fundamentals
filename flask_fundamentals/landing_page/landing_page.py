from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos')
def dojos():
    return render_template('dojos.html')

@app.route('/users', methods=["POST"])
def process():
    print request.form['dojo']
    return redirect('/')


app.run(debug=True)
