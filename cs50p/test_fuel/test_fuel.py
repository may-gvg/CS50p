import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("1 / 4") == 25


def test_convert2():
    with pytest.raises(ZeroDivisionError):
        assert convert("5 / 0") == True


def test_convert3():
    with pytest.raises(ValueError):
        assert convert("nice / one") == True


def test_gauge():
    assert gauge(25) == "25%"


def test_gauge1():
    assert gauge(99) == "F"


def test_gauge2():
    assert gauge(1) == "E"
