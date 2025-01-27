#!/usr/bin/python3
""" Starts a web app using flask, listening on port 5000 """

from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hell0():
    """returns greeting when route is called"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns hbnb when route hbnb is called"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
