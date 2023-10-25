from seasons import check_date
import pytest


def test_get_date():
    with pytest.raises(SystemExit):
        check_date("January 1, 1999")
    with pytest.raises(SystemExit):
        check_date("10100-02-12")
    with pytest.raises(SystemExit):
        check_date("1999-14-1")
    with pytest.raises(SystemExit):
        check_date("1999-02-36")

    assert check_date("1991-05-23") == "1991-05-23"
