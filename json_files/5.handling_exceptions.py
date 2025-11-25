import json

try:
    with open('nonexistent.json', mode='r') as jsonfile:
        data = json.load(jsonfile)
        print(data)

except FileNotFoundError:
    print("File not found")
except json.JSONDecodeError:
    print("Error occurred while decoding JSON data")