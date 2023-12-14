from selenium.webdriver.common.by import By


class AccountReg:
    textbox_Fname_ID="input-firstname"
    textbox_Lname_ID="input-lastname"
    textbox_Email_ID="input-email"
    text_Password_ID="input-password"
    radiobutton_subscribe_Xpath="//input[@id='input-newsletter-yes']"
    checkbox_Agree_Xpath="//input[@name='agree']"
    button_continue_Xpath="//button[normalize-space()='Continue']"
    def  __init__(self,driver):
        self.driver= driver
    def firstname(self,Fname):
        firstname=self.driver.find_element(By.ID,self.textbox_Fname_ID)
        firstname.send_keys(Fname)
    def lastname(self,Lname):
        lastname = self.driver.find_element(By.ID, self.textbox_Lname_ID)
        lastname.send_keys(Lname)
    def email(self,Email):
        email = self.driver.find_element(By.ID, self.textbox_Email_ID)
        email.send_keys(Email)
    def password(self,pwd):
        password = self.driver.find_element(By.ID, self.text_Password_ID)
        password.send_keys(pwd)
    def subscribe(self):
        self.driver.find_element(By.XPATH, self.radiobutton_subscribe_Xpath).click()
    def agree(self):
        self.driver.find_element(By.XPATH, self.checkbox_Agree_Xpath).click()
    def register(self):
        self.driver.find_element(By.XPATH, self.button_continue_Xpath).click()



