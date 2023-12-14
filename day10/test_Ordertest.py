import pytest


class TestClass:

    @pytest.mark.four
    def test_d(self):
        print("this is test D")

    @pytest.mark.three
    def test_c(self):
        print("this is test C")

    @pytest.mark.one
    def test_a(self):
        print("this is test A")

    @pytest.mark.five
    def test_e(self):
        print("this is test E")

    @pytest.mark.two
    def test_b(self):
        print("this is test B")
