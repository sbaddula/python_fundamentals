#Nested if statements
number = 2

if number > 10:
    print("number is greater than 10")
    if number % 2 == 0:
        print("number is even")
    else:
        print("number is odd")
else:
    print("number is less than 10")
