import json

with open('example.json', mode='r') as jsonfile:
    data = json.load(jsonfile)
    print(data)