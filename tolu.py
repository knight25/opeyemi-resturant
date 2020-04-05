from flask import Flask, render_template, redirect, url_for, session, request
from flask_bootstrap import Bootstrap


tolu = Flask(__name__)
Bootstrap(tolu)

@tolu.route('/')
def index():
    return render_template("index.html")

@tolu.route('/tops')
def tops():
    return render_template("tops.html")

@tolu.route('/tops2')
def tops2():
    return render_template("tops2.html")

@tolu.route('/tops3')
def tops3():
    return render_template("tops3.html")

if __name__ == '__main__':
    tolu.run(debug=True)