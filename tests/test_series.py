from math_series import __version__
from math_series.series import *


def test_version():
    assert __version__ == '0.1.0'


def test_fibonacci():
    expected = 5
    actual = fibonacci(5)
    assert actual == expected


def test_fibonacci3():
    assert fibonacci(7) == 13


def test_lucas():
    expected = 4
    actual = lucas(3)
    assert actual == expected


def test_lucas3():
    expected = 29
    actual = lucas(7)
    assert actual == expected


def test_sum_series():
    assert sum_series(2) == 1


def test_sum_series2():
    expected = 17
    actual = sum_series(7, 3, 7)
    assert actual == expected
