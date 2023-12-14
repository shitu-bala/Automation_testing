from selenium import  webdriver
from selenium.webdriver.common.by import By

class PageObject:
    textbox_username_ID= "Email"
    textbox_password_ID="Password"
    button_login_Xpath= "//button[normalize-space()='Log in']"

    def __init__(self,driver):
        self.driver = driver
    def setusername(self,username):
       usernametext=self.driver.find_element(By.ID,self.textbox_username_ID)
       usernametext.clear()
       usernametext.send_keys(username)
    def setpassword(self,pwd):
        userpasswordtext=self.driver.find_element(By.ID,self.textbox_password_ID)
        userpasswordtext.clear()
        userpasswordtext.send_keys(pwd)
    def clicklogin(self):
        self.driver.find_element(By.XPATH,self.button_login_Xpath).click()
        