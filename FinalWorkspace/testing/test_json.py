import json
import os


os.chdir("C:\\Users\\ASUS\\Downloads\\Python\\finalworkspace\\testing")

with open("inventory.json", "r", encoding='utf-8') as f:
    data = json.load(f)

print(data['items'][0]['id'])

data['items'][0]['amount'] += 10

with open('inventory.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)


with open('user.json', 'r', encoding='utf-8') as file:
    user = json.load(file)

new_user = {
    "user_name": "Aomsub",
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

with open('user.json', 'w', encoding='utf-8') as file:
    json.dump(user, file, indent=2)

print("scissors" in data['name'])