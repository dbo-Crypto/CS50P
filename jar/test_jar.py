from jar import Jar
import pytest


def test_init():
    jar = Jar()


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(10, 0)
    jar.deposit(1)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.deposit(15)


def test_withdraw():
    jar = Jar(10, 0)
    jar.deposit(7)
    jar.withdraw(5)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar.withdraw(15)
