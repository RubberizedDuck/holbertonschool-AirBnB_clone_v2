#!/usr/bin/python3
"""
starts a flask web app listening on port 5000
"""


from flask import Flask, render_template
from models import storage
app = Flask(__name__, template_folder="templates")


@app.teardown_appcontext
def app_teardown(exception=None):
    """ Removes SQLAlchemy Session after each request """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def list_state():
    """ rendering template data from state """
    return render_template('8-cities_by_states.html',
                           states=storage.all("State"))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
