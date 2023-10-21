#!/usr/bin/python3
"""
/cities_by_states: page Html
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """
    /states_id: page Html with id
    """
    for state in storage.all("State").values():
        if states_id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """remove session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
