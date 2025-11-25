class Car:
    def __init__(self, make, model, year):
#make, model and year are private attributes which start with "_"
        self._make = make
        self._model = model
        self._year = year

my_car = Car("Ford", "Mustang", 2015)
#You are accessing private attributes of a class which is not good in practice
#it is violation of encapsulation principles and would result in data integrity issues
print(my_car._make, my_car._model, my_car._year)