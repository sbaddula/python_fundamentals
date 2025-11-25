from shape import Rectangle, Circle
from triangle import Triangle

def print_area(shape):
    print(f'area of shape {shape.area()}')

#Create objects of all the classes
rectangle = Rectangle(width=8, height=9)
circle = Circle(6)
triangle = Triangle(base=6, height=7)

#Using the function with different object
print_area(rectangle)
print_area(circle)
print_area(triangle)
