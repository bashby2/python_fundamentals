from flask import Flask, request, redirect, render_template, session
import random
from datetime import datetime

app = Flask(__name__)

app.secret_key = "thisissecret"

@app.route('/')
def index():
    if 'total_gold' not in session:
        session['total_gold'] = 0

    if 'activities' not in session:
        session['activities'] = []

    return render_template('index.html')

@app.route('/makeGold', methods=['POST'])
def makeGold():
    if request.form['generate'] == 'farm':
        total_gold = random.randint(10, 21)
        session['total_gold'] += total_gold
        activities = ("Earned {} golds from the farm. ({})".format(total_gold, datetime.now().strftime('%I:%M %p %d/%m/%Y').lower()))
        # style = "green"
        session['activities'] += [activities]

    elif request.form['generate'] == 'cave':
        total_gold = random.randint(5, 11)
        session['total_gold'] += total_gold
        activities = ("Earned {} golds from the cave. ({})".format(total_gold, datetime.now().strftime('%I:%M %p %d/%m/%Y').lower()))
        session['activities'] += [activities]

    elif request.form['generate'] == 'house':
        total_gold = random.randint(2, 6)
        session['total_gold'] += total_gold
        activities = ("Earned {} golds from the house. ({})".format(total_gold, datetime.now().strftime('%I:%M %p %d/%m/%Y').lower()))
        session['activities'] += [activities]

    elif request.form['generate'] == 'casino':
        chance = random.randint(0, 11)
        if chance > 6:
            total_gold = random.randint(10, 51)
            session['total_gold'] += total_gold
            activities = ("Earned {} golds from the casino! ({})".format(total_gold, datetime.now().strftime('%I:%M %p %d/%m/%Y').lower()))
            session['activities'] += [activities]
        else:
            total_gold = random.randint(10, 50)
            session['total_gold'] -= total_gold
            activities = ("Lost {} golds from the casino....Owch ({})".format(total_gold, datetime.now().strftime('%I:%M %p %d/%m/%Y').lower()))
            session['activities'] += [activities]

    return redirect('/')


@app.route('/reset')
def reset():
    session['total_gold'] = 0
    session['activities'] = []

    return redirect('/')

app.run(debug=True)
