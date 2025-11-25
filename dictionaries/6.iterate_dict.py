person = {
    "name": "John",
    "age": 45,
    "email": "john@gmail.com"
}

#iterate through the keys
for key in person:
    print(key)

#iterate through the values
for value in person.values():
    print(value)

#iterate over both keys and values
for key, value in person.items():
    print(key, ":", value)