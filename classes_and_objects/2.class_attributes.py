class Dog:
    #constructor function
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Create the object with class attributes
my_dog = Dog("Buddy", 3)
print(f"My name is {my_dog.name}, age is {my_dog.age}")

