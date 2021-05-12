def positional(name, age):
    return f"{name=},{age=}"


assert positional("andy", 45) == "name='andy',age=45"

def default_must_be_after_positional(name, age=21):
    return f"{name=},{age=}"


assert default_must_be_after_positional("andy", 25) == "name='andy',age=25"
assert default_must_be_after_positional("andy") == "name='andy',age=21"

def all_keywords(age=21, name="Fred"):
    return f"{name=},{age=}"


assert all_keywords() == "name='Fred',age=21"
assert all_keywords(name="Sue", age=27) == "name='Sue',age=27"

assert all_keywords(name="Julie") == "name='Julie',age=21"
assert all_keywords(42, name="xx") == "name='xx',age=42"

def arbitary_number(*names):
    return ''.join(names)


assert arbitary_number('a', 'b', 'c', 'd') == 'abcd'


def variable_note_order(name, age, *args, size="large", **kwargs):
    return f"{name=},{age=},{args=},{kwargs=}"


assert variable_note_order("andy", 22, ('9', '8', '7'), ('x', 'y'),  a='a', b='b') == \
       "name='andy'," \
       "age=22," \
       "args=(('9', '8', '7'), ('x', 'y'))," \
       "kwargs={'a': 'a', 'b': 'b'}"

assert variable_note_order("andy", 22, ('9', '8', '7'),  a='a', b='b') == \
       "name='andy'," \
       "age=22," \
       "args=(('9', '8', '7'),)," \
       "kwargs={'a': 'a', 'b': 'b'}"
