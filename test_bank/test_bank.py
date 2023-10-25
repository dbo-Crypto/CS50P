from bank import value


def test_value():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("Hell yes") == 20
    assert value("Hola") == 20
    assert value("Hola, Senor?") == 20
    assert value("4") == 100
