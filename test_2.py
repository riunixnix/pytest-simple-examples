import pytest

""" Create Method to calculate formula below with input `number` 
( number + 1) * ( number - 1)
"""


def plus_1(number):
    """ number+1 """
    return number+1


def minus_1(number):
    """ number-1 """
    return number-1


def multiply(number_1, number_2):
    """ number_1 x number_2 """
    return number_1 * number_2


def formula(number):
    """ (number+1) x (number-1) """
    return multiply(
        plus_1(number),
        minus_1(number)
    )

# --- testing code --
@pytest.mark.unit
def test_plus_1():
    assert plus_1(1) == 2


@pytest.mark.unit
def test_minus_1():
    assert minus_1(1) == 0


@pytest.mark.unit
def test_multiply():
    assert multiply(2, 5) == 10


@pytest.mark.integration
def test_formula():
    assert formula(10) == 99
