import pytest
class TestClass:

        @pytest.fixture()  #decoration
        def setup(self):
            print("launching  browser")
            print("open application")
        def test_login(self,setup):
            print("this is first method of login")

        def test_search(self,setup):
            print("this is second method of search")
        def test_advancesearch(self,setup):
            print("this is thirdmethod for advance seach")