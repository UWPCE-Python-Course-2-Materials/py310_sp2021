import math


class Pizza:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    # conceptually, I "belong" to the class (but a subtle point)
    @staticmethod
    def compute_area(radius):
        return math.pi * (radius ** 2)

    def compute_volume(self):
        return self.height * Pizza.compute_area(self.radius) # or self.


p = Pizza(10, 1)
print(p.compute_volume())

print(Pizza.compute_area(12))
