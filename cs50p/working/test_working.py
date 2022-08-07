from working import convert 
import pytest

def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    
    
def test_convert2():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_convert3():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"


def test_convert4():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_convert5():
    with pytest.raises(ValueError):
        assert convert("9 am - 9 pm") == True


def test_convert6():
    with pytest.raises(ValueError):
        assert convert("dupa dupa dupa") == True

def test_convert7():
    with pytest.raises(ValueError):
        assert convert("12:77 pm to 12:60 am") == True
