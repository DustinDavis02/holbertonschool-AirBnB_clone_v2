from flask import Flask, render_template
from models import storage, State, session

app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    session.remove()
    return render_template('states_list.html', states=sorted_states)

@app.teardown_appcontext
def close_storage(error):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
