import pytest


@pytest.mark.parametrize("a,b,final",[(1,5,6),(4,9,13),(3,7,11)])
def test_login(a,b,final):
    assert a+b==final