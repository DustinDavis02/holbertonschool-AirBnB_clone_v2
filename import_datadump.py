from models import storage
from models.state import State
from models.city import City
import json

with open('7-dump', 'r') as f:
    data = json.load(f)

for state_data in data['states']:
    state = State(**state_data)
    storage.new(state)

for city_data in data['cities']:
    city = City(**city_data)
    storage.new(city)

storage.save()
