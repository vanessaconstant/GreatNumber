from crypt import methods
from urllib import request
from flask import Flask, render_template, redirect, session, request

import random
app = Flask(__name__)

app.secret_key = "VGLOR"


@app.route('/')
def startGame():
    if 'num' not in session:
        session['num'] = random.randint(1, 100)
    return render_template("index.html")


@app.route('/guess', methods=['POST'])
def guess():

    session['guessed_number'] = int(request.form['guessed_number'])

    return redirect('/result')


@app.route('/result')
def result():
    if int(session['num']) == session['guessed_number']:
        message = f'Success!! The number was {session["num"]}'
        success = True
    elif int(session['num']) > session['guessed_number']:
        message = 'Too Low!!'
        success = False
    else:
        message = 'Too High!!'
        success = False
    return render_template('result.html', message=message, success=success)


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
