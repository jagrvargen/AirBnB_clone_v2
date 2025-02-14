#!/usr/bin/python3
'''
   This module contains a script which will start a Flask web application and
   display "Hello HBNB!" and "HBNB" from the "/" and "/hbnb" URLs respectively.
   "C <text>" will be displayed by calling /c/<text> where any text can replace
   <text>.
'''
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    return "Hello HBNB!"


@app.route("/hbnb/", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<string:text>/", strict_slashes=False)
def c(text):
    if text:
        new = text.replace("_", " ")
    return "C {}".format(new)


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<string:text>", strict_slashes=False)
def python(text):
    if text:
        new = text.replace("_", " ")
        return "Python {}".format(new)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    if type(n) == int:
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    if type(n) == int:
        return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    if type(n) == int:
        return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
