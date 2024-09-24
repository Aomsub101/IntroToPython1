import json
import os

CURR_PATH = os.getcwd()

with open("inventory.json", "r") as f:
    data = json.load(f)

print(data['items'][0]['id'])

data['items'][0]['amount'] += 10

with open('inventory.json', 'w') as f:
    json.dump(data, f, indent=2)


with open('user_inventory.json', 'r') as file:
    user = json.load(file)

new_user = {
    "name": "Aomsub",
    "Key": 1,
    "items":[
        {
            "item_key":1,
            "item_name":"scissors",
            "amount": 20
        }
    ]
}

user['user'].append(new_user)

with open('user_inventory.json', 'w') as file:
    json.dump(user, file, indent=2)