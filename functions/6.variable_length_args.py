#"Functions accept variable number of arguments using *args and **kwargs"

#function with *args
def add(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

result = add(1, 2, 3, 4, 5, 6, 7, 8)
print(result)

#function with **kwargs
def describe_person(**info):
    for key, value in info.items():
        print(f'{key}: {value}')


#calling function with keyword arguments
describe_person(name="John", age=24, city="London", phone=9940455167)
