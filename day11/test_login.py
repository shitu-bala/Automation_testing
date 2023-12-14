from selenium import webdriver
from pageobjectmodel import PageObject

class Testlogin:
    def test_login(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://admin-demo.nopcommerce.com/login?")
        print(self.driver.title)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.obj=PageObject(self.driver)
        self.obj.setusername("admin@yourstore.com")
        self.obj.setpassword("Admin")
        self.obj.clicklogin()
        self.act_act=self.driver.title
        self.driver.close()
        assert self.act_act=="Your store. Login"

