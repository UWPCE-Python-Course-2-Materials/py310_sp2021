class Vehicle:
    def __init__(self):
        self.wheels = 4
        self.doors = 2

    def move(self):
        return "moving"


truck = Vehicle()
assert truck.wheels == 4
assert truck.move() == "moving"


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.passengers = True

    def move(self):
        return "moving fast"


car = Car()

assert car.passengers is True
assert car.wheels == 4
assert car.move() == "moving fast"
