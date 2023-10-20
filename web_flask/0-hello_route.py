#!/usr/bin/python3
"""
 A script starts a Flask web application:
    web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
You must use the option strict_slashes=False
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello, HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
