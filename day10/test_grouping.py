import pytest


class TestClass:
    @pytest.mark.regression
    def test_search(self):
        print("this is search  method of search")
        assert 1 == 1
    @pytest.mark.sanity
    def test_advancesearch(self):
        print("this is advance search for advance seach")
        assert 1 == 1

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_loginByEmail(self):
        print(" this is login by Email...")
        assert True == True

    @pytest.mark.regression
    def test_loginByFacebool(self):
        print(" this is login by Facebook...")
        assert True == True

    @pytest.mark.regression
    def test_loginBytwitter(self):
        print(" this is login by Twitter...")
        assert True == True

    @pytest.mark.regression
    def test_SingupByEmail(self):
        print(" this is  Singup by Email...")
        assert True == True

    @pytest.mark.sanity
    def test_SingupByFacebool(self):
        print(" this is  Singup by Facebook...")
        assert True == True
