import py310.lesson04.my_mod


def test_my_func():
    test_val1, test_val2 = 2, 3
    expected = 6
    actual = py310.lesson04.my_mod.my_func(test_val1, test_val2)
    assert expected == actual


def adder(num1, num2):
    return num1, num2


def test_adder():
    result = adder(2, 3)
    assert result[1] == 9


def myfunc(atuple):
    pass
