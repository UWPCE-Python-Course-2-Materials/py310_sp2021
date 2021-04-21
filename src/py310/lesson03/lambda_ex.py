def increment_by_one(number):
    return number + 1


assert (lambda x: x + 1)(2) == increment_by_one(2)

assert (lambda x, y: x + y)(10, 20) == 30
