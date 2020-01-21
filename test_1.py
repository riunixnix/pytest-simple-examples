""" Simple Example """


def plus_1(number):
    """ number+1 """
    return number+1

# -----Testing------------


def test_plus_1():
    """ chekc if plus_1 method works properly """
    assert plus_1(1) == 2
