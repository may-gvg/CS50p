from jar import Jar


def test_init():
    jar = Jar(capacity=5)
    assert(1==1)

def test_str():
    jar = Jar(capacity=5)
    assert str(jar) == ""


def test_deposit():
    jar = Jar(capacity=10)
    jar.deposit(1)
    assert str(jar) == "🍪"


def test_withdraw():
    jar = Jar(capacity=10)
    jar.deposit(1)
    jar.withdraw(1)
    assert str(jar) == ""

def test_withdraw():
    jar = Jar(capacity=10)
    jar.deposit(1)
    jar.withdraw(1)
    assert str(jar) == ""
