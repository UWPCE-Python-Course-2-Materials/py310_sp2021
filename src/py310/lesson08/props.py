class Person:
    def __init__(self, first_name, last_name):
        self.last_name = last_name
        self.first_name = first_name

    @property
    def full_name(self):
        return f"{self.first_name} {andy.last_name}"

    @property
    def name_for_sort(self):
        return f"{self.last_name}, {andy.first_name}"


andy = Person('andy', 'miles')

# good python - it's just data
assert andy.first_name == 'andy' 
assert andy.last_name == 'miles' 


# so is this, really
assert andy.full_name == 'andy miles'
assert andy.name_for_sort == 'miles, andy'

# but why not andy.name_for_sort() - subtle, data vs. doing

# -----------------------------------------------------------------------------


class PersonB:
    def __init__(self, first_name, last_name):
        self._last_name = last_name
        self.first_name = first_name

    @property
    def full_name(self):
        return f"{self.first_name} {andy._last_name}"

    @property
    def name_for_sort(self):
        return f"{self._last_name}, {andy.first_name}"

    @property
    def last_name(self):
        return self._last_name.capitalize()

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name


andyb = PersonB('andy', 'miles')

# good python - it's just data
assert andyb.first_name == 'andy' 
assert andyb._last_name == 'miles' 


# so is this, really
assert andyb.full_name == 'andy miles'
assert andyb.name_for_sort == 'miles, andy'


# properties can preserve contracts - say capitalize() for a name


andyb.last_name = "myles"
assert andyb.last_name == "Myles"
