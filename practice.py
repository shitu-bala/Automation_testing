from selenium import webdriver


class Login:
    def datalogin(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://admin-demo.nopcommerce.com/login?")
        obj=self.driver.title
        print(obj)
A1= Login()
A1.datalogin()
