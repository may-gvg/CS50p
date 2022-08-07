from twttr import shorten


def test_shorten():
    assert shorten("Owitter.1") == "wttr.1"


