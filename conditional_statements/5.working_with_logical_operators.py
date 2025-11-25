#using logical operators
number = 8

if number > 5 and number < 10:
    print("number is in between 5 and 10")

if number < 5 or number > 10:
    print("number is either less than 5 or greater than 10")

if not (number > 10):
    print("number is not greater than 10")