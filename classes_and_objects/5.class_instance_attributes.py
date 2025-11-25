class Dog:
    #the below is a class attribute
    species = "Canis familiaris" #Domestic Dog
    #constructor
    def __init__(self, name, age):
        self.name = name #instance attribute
        self.age = age #instance attribute


#create an object
dog1 = Dog("Buddy", 5)
dog2 = Dog("Lucy", 3)

print("Dog 1 species: ", dog1.species)
print("Dog 2 species: ", dog2.species)
print(f"Dog1 {dog1.name} age: {dog1.age} and it's species is {dog1.species}.")
print(f"Dog2 {dog2.name} age: {dog2.age} and it's species is {dog2.species}.")
