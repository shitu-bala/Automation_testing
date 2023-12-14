import  pytest
from selenium import  webdriver
from selenium.webdriver.common.by import By


class TestClass:
    @pytest.mark.parametrize("user,pwd",[("Admin","admin123"),("adm","ad124")])
    def test_login(self, user, pwd):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(user)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(pwd)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        try:
           self.status=self.driver.find_element(By.XPATH,"//h6[normalize-space()='Dashboard']").is_displayed()
           self.driver.close()
           assert self.status == True

        except:
            self.driver.close()
            assert False
