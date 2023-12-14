import pytest


class TestClass:
    @pytest.mark.parametrize('num1,num2',[(4,4),(5,5),(2,9),(13,13)])
    def test_calculation(self, num1,num2):
        assert num1==num2