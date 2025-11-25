try:
    num = int(input("Enter a number: "))
    result = 10 / num

except(ZeroDivisionError, ValueError) as e:
    print(f"Error: {e}")
else:
    print(f'result: {result}')
finally:
    print("Closing code, this will be always executed")