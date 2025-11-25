import json

data = {
        "name": "Mark",
        "age": 30,
        "address": {
            "city": "New York",
            "state": "NY",
            "country": "USA"
      }
}

with open("output.json", "w") as jsonfile:
    json.dump(data, jsonfile, indent=4)

jsonfile.close()