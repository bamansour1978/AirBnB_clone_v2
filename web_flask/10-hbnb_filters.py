#!/usr/bin/python3
"""
/hbnb_filteers: page Html
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays an HTML page with a list of all States.

    States are sorted by name.
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters", state=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
    """remove session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
