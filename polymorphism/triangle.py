from shape import Shape

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

triangle = Triangle(base=4, height=5)
#print(f'The area of triangle is {triangle.area()}')