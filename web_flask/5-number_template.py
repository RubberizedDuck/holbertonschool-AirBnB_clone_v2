#!/usr/bin/python3
"""
Starts a web app using flask, listening on port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable
(replace underscore _ symbols with a space )
You must use the option strict_slashes=False in your route definition
"""


from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hell0():
    """returns greeting when route is called"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns hbnb when route hbnb is called"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """displays url text on page"""
    return "C " + text.replace("_", " ")


@app.route("/python/", strict_slashes=False, defaults={'text': "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """displays default text if no text is passed"""
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def is_it_a_number(n):
    """ returns a number only if n is an integer """
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ returns a number only if n is an int, from the template """
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
