import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin:

    def test_chromlogin(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.NAME,"username").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        assert self.driver.title=="OrangeHRM"
        self.driver.quit()

    def test_Edgelogin(self):
        self.driver = webdriver.Edge()
        self.driver.implicitly_wait(10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        assert self.driver.title =="OrangeHRM"
        self.driver.quit()

    def test_firefoxlogin(self):

        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get(" ")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        assert self.driver.title =="OrangeHRM"
        self.driver.quit()
