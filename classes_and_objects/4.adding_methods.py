class Dog:
    #constructor function
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def sound(self, sound):
        return f"{self.name} says {sound}!"


#create the instance and call the methods
my_dog = Dog("Buddy", 5)
print(my_dog.description())
print(my_dog.sound("Woof Woof"))