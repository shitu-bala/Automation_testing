from selenium import webdriver
from pageobjopencart import AccountReg

class TestRegister:
    def test_login(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://demo.opencart.com/index.php?route=account/register&language=en-gb")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.obj1= AccountReg(self.driver)
        self.obj1.firstname("Ayggghjhaan")
        self.obj1.lastname("Vermmba")
        self.obj1.email("av208232hggg@gmail.com")
        self.obj1.password("Apr@2017")
        self.obj1.subscribe()
        self.obj1.agree()
        self.obj1.register()
        self.driver.close()

