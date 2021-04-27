import json

dictionary_variable = {'k': 'value'}

with open('file.json', 'w+') as f:
    json.dump(dictionary_variable, f)


dictionary_variable = json.loads(open('file.json').read())
assert dictionary_variable == {'k': 'value'}
