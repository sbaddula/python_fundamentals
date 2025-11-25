class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_age(self):
        return self._age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        if age > 0:
            self._age = age
        else:
            print("age must be greater than 0")


person = Person("John", 18)
print(f'{person.get_name()} is {person.get_age()} years old.')

#updating age with a setter
person.set_age(25)
print(f'{person.get_name()} is {person.get_age()} years old.')

#setting a negative age
person.set_age(-25)

#delibrately accessing the private attribute and setting the value
#it causes integrity issue, you will see the value getting set incorrectly
person._age = -20
print(f'{person.get_name()} is {person.get_age()} years old.')
