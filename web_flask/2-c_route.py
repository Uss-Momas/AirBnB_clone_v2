#!/usr/bin/python3
"""hello route flask"""

from flask import Flask

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
def c_fun(text):
    """receive a param process and return it"""
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
