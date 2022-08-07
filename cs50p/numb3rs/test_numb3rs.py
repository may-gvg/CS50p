import pytest
from numb3rs import validate


def test_validate():
    assert validate("125.125.125.0") == True



def test_validate1():
    assert validate("300.125.125.0") == False


def test_validate3():
    assert validate("dupa.dupa.dupa.dupa") == False


def test_validate4():
    assert validate("1") == False

def test_validate5():
    assert validate("127.999.999.999") == False
