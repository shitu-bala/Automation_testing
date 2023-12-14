import pytest
@pytest.fixture(params=["arun","ayaan"])
def demo_fixture(request):
    print(request.param)
def test_login(demo_fixture):
    print("login succefull ......")