from mypkg.funcs import plus


def test_plus():
    assert plus(1, 2) == 3
    assert plus(3, 2) == 5