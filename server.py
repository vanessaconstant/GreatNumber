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
def result():

    session['guessed_number'] = int(request.form['guessed_number'])

    if session['num'] == session['guessed_number']:
        session['message'] = f'Success!! The number was {session["num"]}'
        session['success'] = True
    elif int(session['num']) > session['guessed_number']:
        session['message'] = 'Too Low!!'
        session['success'] = False
    else:
        session['message'] = 'Too High!!'
        session['success'] = False
    return redirect('/')


@ app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
