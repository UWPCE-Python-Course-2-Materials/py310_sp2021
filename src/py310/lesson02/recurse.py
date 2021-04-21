def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)


assert factorial(3) == 6
assert factorial(5) == 120


explain = 5 * (5-1) * (4-1) * (3-1) * (2-1)

assert explain == factorial(5)
