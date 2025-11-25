import json

with open('example.json', mode='r') as jsonfile:
    data = json.load(jsonfile)

for entry in data:
    print(f"Name: {entry['name']}")
    print(f"Age: {entry['age']}")
    print(f"City: {entry['address']['city']}")
    print(f"State: {entry['address']['state']}")

jsonfile.close()