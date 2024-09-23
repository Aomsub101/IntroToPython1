import json
import os

CURR_PATH = os.getcwd()

with open("inventory.json", "r") as f:
    data = json.load(f)

print(data['items'][0]['id'])

data['items'][0]['amount'] += 10

with open('inventory.json', 'w') as f:
    json.dump(data, f, indent=2)