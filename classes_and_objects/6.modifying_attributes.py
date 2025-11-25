class Dog:
    #automatically done for you
    #local_name = None
    #local_age = None

    def __init__(self, name, age):
        self.local_name = name
        self.local_age = age

#modifying the attributes, setters help you for it
    def set_age(self, age):
        self.local_age = age

    def set_name(self, name):
        self.local_name = name

#Create the object
my_dog = Dog("Buddy", 5)
print(f"original age: {my_dog.local_age}")
my_dog.set_age(6)
print(f"new age: {my_dog.local_age}")
print(f"original name: {my_dog.local_name}")
my_dog.set_name("Mate")
print(f"new name: {my_dog.local_name}")
