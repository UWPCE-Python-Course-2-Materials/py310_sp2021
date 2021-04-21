def dont_learn_this_way():
    print(len("xxxxx"))
    print(f"{len('jjj')}")


def do_learn_this_way():
    assert 1 == 1
    assert 1 + 1 == 2
    assert '1' + '1' == '11'
    assert 2 * 3 == 6
    assert 2 * '3' == '33'
    assert len('jjj') == 3


def record_my_learning():
    dont_learn_this_way()
    do_learn_this_way()


if __name__ == "__main__":
    record_my_learning()
