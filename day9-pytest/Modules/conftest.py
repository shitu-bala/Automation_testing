import pytest

@pytest.fixture()  # decoration
def setup():
    print("launching  browser ...")
    print("open application")
    yield
    print("browser is closing...")
