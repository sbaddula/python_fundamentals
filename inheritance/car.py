#You are saying import from the file vehicle the class Vehicle
from inheritance.vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, model, num_of_doors):
        super().__init__(brand, model)
        self.num_of_doors = num_of_doors

    def play_radio(self):
        return "Play Radio"


car = Car("Toyota", "Corolla", 4)
print(car)
print(car.start_engine())
print(car.play_radio())
print(car.stop_engine())
