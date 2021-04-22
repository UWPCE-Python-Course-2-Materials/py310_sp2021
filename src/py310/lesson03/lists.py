names = [
    'andy',
    'sue',
    'fred',
    'jim',
    'carol',
]

assert str(type(names)) == "<class 'list'>"
assert names == ['andy', 'sue', 'fred', 'jim', 'carol']

names.pop(1)
assert names == ['andy', 'fred', 'jim', 'carol']

names.append('sally')
assert names == ['andy', 'fred', 'jim', 'carol', 'sally']

sorted(names)
assert names == ['andy', 'fred', 'jim', 'carol', 'sally']

names.sort()
assert names == ['andy', 'carol', 'fred', 'jim', 'sally']

names.append('fred')
assert names.count('fred') == 2
assert names.index('jim') == 3
assert names.index('andy') == 0
assert 'fred' in names
assert 'xxx' not in names

assert "abc,3df,uuyyttr".split(',') == ['abc', '3df', 'uuyyttr']
assert ''.join(['1', 'ddd', '888bb']) == '1ddd888bb'
