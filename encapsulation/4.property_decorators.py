class Car:
    def __init__(self, make, model, year):
#make, model and year are private attributes
        self._make = make
        self._model = model
        self._year = year

#@property works as getter
    @property
    def year(self):
        return self._year
#below works as setter
    @year.setter
    def year(self, year):
        if year > 1900:
            self._year = year
        else:
            print("Invalid year for the car")


my_car = Car("Ford", "Mustang", 2015)
my_car.year = 2018
print("updated car year is", my_car.year )

my_car.year = 1895
