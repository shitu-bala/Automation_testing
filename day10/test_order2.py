
import pytest



class TestClass:
    @pytest.mark.run(order=4)
    def test_d(self):
        print("this is test D......")


    @pytest.mark.run(order=3)
    def test_c(self):
        print("this is test C.......")


    @pytest.mark.run(order=1)
    def test_a(self):
        print("this is test A.....")

    @pytest.mark.run(order=5)
    def test_e(self):
        print("this is test E........")


    @pytest.mark.run(order=2)
    def test_b(self):
        print("this is test B......")

