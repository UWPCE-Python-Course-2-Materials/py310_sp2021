import math


class Circle:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    # conceptually, I "belong" to the class (but a subtle point)
    @staticmethod
    def compute_area(radius):
        return math.pi * (radius ** 2)

    def compute_volume(self):
        return self.height * Circle.compute_area(self.radius) # or self.


c = Circle(10, 1)
print(c.compute_volume())

print(Circle.compute_area(12))
