try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Division by Zero is not allowed")