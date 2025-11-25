class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
         return f"Vehicle {self.brand} has started"

    def stop_engine(self):
        return f"Vehicle {self.brand} has stopped"

#used to define a human-readable string representation of an object.
#It’s what gets called when you use print on an instance

    def __str__(self):
        return f"{self.brand} {self.model}"

#vehicle = Vehicle("BMW", "5 Series")
#print(vehicle)