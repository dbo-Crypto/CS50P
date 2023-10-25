from um import count


def test_um():
    assert count("Hello, there") == 0
    assert count("um") == 1
    assert count("Hello,um there") == 1
    assert count("Hello um, there") == 1
    assert count("um Hello, um there") == 2
    assert (
        count(
            "Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?"
        )
        == 2
    )
