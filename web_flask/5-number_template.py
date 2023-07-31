#!/usr/bin/python3
"""hello route flask"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """hello world from application"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display only HBNB"""
    return "HBNB"


@app.route("/c/<string:text>", strict_slashes=False)
def c(text):
    """receive a param process and return it"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Optional parameter"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """verify if n is integer"""
    return "{} is a number".format(int(n))


@app.route("/number_template/<int:n>", strict_slashes=False, )
def number_template(n):
    """Jinja displaying the parameter"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
