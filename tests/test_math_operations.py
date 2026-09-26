import math
import pytest
from src.math_operations import add, subtract, multiply, divide, modulus, power, square


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 7) == 21


def test_divide():
    assert divide(8, 2) == 4


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

def test_modulus():
    assert modulus(5, 3) == 2

def test_power():
    assert power(2, 4) == 16

def test_absolute():
    assert abs(-6) == 6

def test_square():
    assert square(9) == 81