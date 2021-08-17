from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = "something "


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def process():
    session['form'] = request.form
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    print(session['form'])
    return redirect('/show')


@app.route('/show')
def show():
    return render_template('show.html')


if __name__ == "__main__":
    app.run(debug=True)
