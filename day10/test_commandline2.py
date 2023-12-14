from selenium.webdriver.common.by import By


class TestClass:
    def test_logo(self,setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        try:
            self.status = self.driver.find_element(By.XPATH, "//img[@alt='company-branding']").is_displayed()
            self.driver.close()
            assert self.status==True

        except:

              self.driver.close()
              assert  False



    def test_login(self,setup):

        print(setup)
        self.driver= setup
        self.driver.implicitly_wait(10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        try:
           self.status=self.driver.find_element(By.XPATH,"//h6[normalize-space()='Dashboard']").is_displayed()
           self.driver.close()
           assert self.status == True

        except:
            self.driver.close()
            assert False
