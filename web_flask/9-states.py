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


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def list_custom_state(state_id=None):
    """ rendering template data from state """
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
