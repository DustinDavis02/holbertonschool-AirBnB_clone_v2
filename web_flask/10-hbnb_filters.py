#!/usr/bin/python3
"""HBNB filters"""
from flask import Flask, request, render_template
from markupsafe import escape
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """Display HTML page"""
    states = storage.all('State')
    amenities = storage.all('Amenity')
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(args):
    """Remove current SQL Alchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(debug=True  , host='0.0.0.0', port='5000')