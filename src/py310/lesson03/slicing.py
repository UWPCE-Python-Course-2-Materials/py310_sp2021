names = [
    'andy',
    'sue',
    'fred',
    'jim',
    'carol'
]

assert names[0] == 'andy'
assert names[4] == 'carol'
assert names[-1] == 'carol'
assert names[-2] == 'jim'
assert names[0:2] == ['andy', 'sue']
assert names[1:2] == ['sue']
assert names[3:] == ['jim', 'carol']
assert names[-2:] == ['jim', 'carol']
assert names[::-1] == ['carol', 'jim', 'fred', 'sue', 'andy']
assert names == ['andy', 'sue', 'fred', 'jim', 'carol']
names.reverse()
assert names == ['carol', 'jim', 'fred', 'sue', 'andy']
assert names[1:5:2] == ['jim', 'sue']
