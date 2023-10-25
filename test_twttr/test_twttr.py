from twttr import shorten

def test_shorten():
    assert shorten("test") == "tst"
    assert shorten("t4st-testing") == "t4st-tstng"
    assert shorten("Hello, World") == "Hll, Wrld"
    assert shorten("TEST") == "TST"