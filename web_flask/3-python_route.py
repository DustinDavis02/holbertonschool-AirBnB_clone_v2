#!/usr/bin/python3
"""This script starts a Flask web application and defines the routes:"""

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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Displays "C <text>" when the "/c/<text>" URL is requested,
    where <text> is the value of the text variable
    with underscores replaced with spaces."""
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Displays "Python <text>" when the URL is requested,
    <text> is the value of the variable underscores replaced with spaces,
    or the default value "is cool" if text is not provided."""
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
