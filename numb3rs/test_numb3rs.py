from numb3rs import validate
import pytest


def test_validate():
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("102.555.555.555") == False
