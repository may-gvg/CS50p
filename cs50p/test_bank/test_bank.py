from bank import value


def test_value():
    assert value("hello") == 0


def test_value2():
    assert value("dupa") == 100

def test_value3():
    assert value("What’s up") == 100




def test_value4():
    assert value("Hello") == 0


def test_value5():
    assert value(" hurray maciek ") == 100

def test_value6():
    assert value(" hurray maciek ") == 100


def test_value7():
    assert value("hurray") == 20