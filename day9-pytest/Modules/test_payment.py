import pytest

class TestPayment:
    def test_paybydollar(self,setup):
        print(" this is  dollar payment method...")
        assert True == True

    def test_paybyrupees(self,setup):
        print(" this is  Rupee payment method.")
        assert True == True

