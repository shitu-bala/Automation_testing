import pytest


class TestClass:
    @pytest.mark.skip
    def test_search(self):
        print("this is search  method of search")
        assert 1 == 1
    @pytest.mark.skip
    def test_advancesearch(self):
        print("this is advance search for advance seach")
        assert 1 == 1

    def test_loginByEmail(self):
        print(" this is login by Email...")
        assert True == True

    def test_loginByFacebool(self):
        print(" this is login by Facebook...")
        assert True == True

    def test_loginBytwitter(self):
        print(" this is login by Twitter...")
        assert True == True

    def test_SingupByEmail(self):
        print(" this is  Singup by Email...")
        assert True == True

    def test_SingupByFacebool(self):
        print(" this is  Singup by Facebook...")
        assert True == True

    def test_SingupBytwitter(self):
        print(" this is Singup by Twitter...")
        assert True == True


    def test_paybydollar(self):
        print(" this is  dollar payment method...")
        assert True == True


    def test_paybyrupees(self):
        print(" this is  Rupee payment method.")
        assert True == True
