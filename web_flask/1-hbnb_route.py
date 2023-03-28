#!/usr/bin/python3
"""This script starts a Flask web application and defines the following routes:
- "/" : display "Hello HBNB!"
- "/hbnb" : display "HBNB"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays "Hello HBNB!" when the root URL is requested."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays "HBNB" when the "/hbnb" URL is requested."""
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
