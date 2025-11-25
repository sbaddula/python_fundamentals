class Car:
    def __init__(self, make, model, year):
#make, model and year are public attributes
        self.make = make
        self.model = model
        self.year = year


my_car = Car("Ford", "Mustang", 1999)
#public attributes of a class can be accessed outside
print(my_car.make, my_car.model, my_car.year)