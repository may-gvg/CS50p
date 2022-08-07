from plates import is_valid


def test_is_valid():
    assert is_valid("SCI923") == True


def test_is_valid2():
    assert is_valid("S") == False


def test_is_valid3():
    assert is_valid("SSSSSSSSSSSSS") == False

def test_is_valid4():
    assert is_valid("CS50") == True

def test_is_valid5():
    assert is_valid("HELLO, WORLD") == False

def test_is_valid6():
    assert is_valid("50") == False

def test_is_valid7():
    assert is_valid("12Mac50") == False

def test_is_valid8():
    assert is_valid("CS05") == False

def test_is_valid9():
    assert is_valid("HELLO") == True

def test_is_valid10():
    assert is_valid("AAA222") == True

def test_is_valid11():
    assert is_valid("AAA22A") == False

def test_is_valid12():
    assert is_valid("AAA022") == False
    
def test_is_valid13():
    assert is_valid("AAA 22") == False