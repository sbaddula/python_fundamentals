import json

#json string
json_string = '{"name": "Luke", "age": 28, "address": {"city": "Los Angeles", "state": "CA"}}'

data = json.loads(json_string)
print(data)

json_string_formatted = json.dumps(data, indent=4)
print(json_string_formatted)
