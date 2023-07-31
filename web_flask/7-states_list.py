#!/usr/bin/python3
"""
List state
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/states_list")
def states_list():
    """
    Method to handle the listing of the states
    """
    from models import storage
    from models.state import State

    states = storage.all(State)
    states = states.items()
    states = list(states)
    states = [obj for key, obj in states]

    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy session"""
    from models import storage
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
