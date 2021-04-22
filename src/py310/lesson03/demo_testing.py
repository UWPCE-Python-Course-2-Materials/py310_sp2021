def adder(lhs, rhs):
    return lhs + rhs


def test_adder_simple_add():
    assert adder(9, 10) == 19


def test_adder_floats():
    assert adder(1.1, 2.3) == 3.4
