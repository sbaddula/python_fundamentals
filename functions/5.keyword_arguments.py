#function with multiple parameters
def describe_person(name, age, city):
    print(f'{name} is {age} years old and lives in {city}.')


#calling function with keyword arguments
describe_person(name="John", age=24, city="London")
describe_person(city="New York", name="Mark", age=34)
