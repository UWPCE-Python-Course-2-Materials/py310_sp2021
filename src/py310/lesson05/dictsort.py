people = {1: 'fred', 0: 'harry', 9: 'andy'}

assert sorted(people.keys()) == [0, 1, 9]

assert sorted(people.values()) == ['andy', 'fred', 'harry']

assert sorted(people.items()) == [(0, 'harry'), (1, 'fred'), (9, 'andy')]

assert dict(sorted(people.items())) == {0: 'harry', 1: 'fred', 9: 'andy'}

person = people.get(1, None)
assert person == 'fred'

person = people.get(8, None)
assert person is None
