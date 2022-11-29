#!/usr/bin/python3
"""
starts a flask web app listening on port 5000
"""


from flask import Flask, render_template
from models import storage
app = Flask(__name__, template_folder="templates")


@app.teardown_appcontext
def app_teardown(exception):
    """ Removes SQLAlchemy Session after each request """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def show_statesCity_amenities():
    """ retrieves States from DB storage and show in html """
    states = storage.all("State")
    amenities = storage.all("Amenities")
    return render_template("10-hbnb_filters.html",
                           states=states,
                           amenities=amenities)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
