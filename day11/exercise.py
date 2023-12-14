from selenium import webdriver
from pageobjopencart import AccountReg

class Register:
    def login(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://demo.opencart.com/index.php?route=account/register&language=en-gb")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.obj1= AccountReg(self.driver)
        self.obj1.firstname("Ayaan")
        self.obj1.lastname("Verma")
        self.obj1.email("av208232@gmail.com")
        self.obj1.password("Apr@2017")
        self.obj1.subscribe()
        self.obj1.agree()
        self.obj1.register()
        self.driver.close()
ab=Register()

ab.login()
