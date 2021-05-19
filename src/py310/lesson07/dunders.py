class Car:
    def __init__(self, owner, value):
        self.owner = owner
        self.value = value

    """def __repr__(self):
        return 'Car|{!r}|{!r}'.format(self.owner, self.value)"""

    """def __str__(self):
        return 'Car owned by {} has current value: {}'.format(
            self.owner, self.value)"""

    def __len__(self):
        return 42

ford = Car("Andy", 35_000)

print(ford)
print(str(ford))
print(repr(ford))
print(len(ford))
