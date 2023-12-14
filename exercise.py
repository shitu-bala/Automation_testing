import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin:

    def chromlogin(self):

        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()

        assert self.driver.title=="OrangeHRM"






obj=TestLogin()
obj.chromlogin()