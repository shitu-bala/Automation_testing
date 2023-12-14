import pytest


class TestClass:

    @pytest.mark.dependency()
    def test_openapp(self):
        assert False

    @pytest.mark.dependency(depends=['TestClass::test_openapp'])
    def test_login(self):
        assert True

    @pytest.mark.dependency(depends=['TestClass::test_login'])
    def test_search(self):
        assert True

    @pytest.mark.dependency(depends=['TestClass::test_search', 'TestClass::login'])
    def test_advsearch(self):
        assert True

    @pytest.mark.dependency(depends=['TestClass::test_login'])
    def test_logout(self):
        assert True
