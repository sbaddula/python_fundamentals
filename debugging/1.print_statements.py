def divide(x, y):
    print(f'{x} divided by {y}')
    if y == 0:
        print('division by zero error')
        return None
    result = x / y
    print(f'{x} divided by {y} = {result}')
    return result

divide(10, 5)
#divide(10, -5)
#divide(10, 0)



