import pdb

def divide(x, y):
    pdb.set_trace()
    if y == 0:
        return "Error: division by zero"
    return x / y


print(divide(5, 0))