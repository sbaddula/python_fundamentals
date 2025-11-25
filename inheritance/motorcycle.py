from inheritance.vehicle import Vehicle


class Motorcycle(Vehicle):
    def __init__(self, brand, model, type_motorcycle):
        super().__init__(brand, model)
        self.type_motorcycle = type_motorcycle

    def wheelie(self):
        return "Doing a wheelie"


motorcycle = Motorcycle("Yamaha", "MT-07", "Sport")
print(motorcycle.start_engine())
print(motorcycle.wheelie())
print(motorcycle.stop_engine())
