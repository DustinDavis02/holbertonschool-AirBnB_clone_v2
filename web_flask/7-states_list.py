#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from markupsafe import escape

app = Flask(__name__)



@app.route('/states_list', strict_slashes=False)
def display_states_list():
    """Displays a list of all State objects present in the DBStorage sorted by name"""
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown_session(args):
    """Closes the storage session after each request"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)