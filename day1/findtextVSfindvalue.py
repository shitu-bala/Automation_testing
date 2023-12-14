import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj = Service("C:\webdrivers\chromedriver.exe")

driver = webdriver.Chrome(service= serv_obj)
driver.get("https://demo.nopcommerce.com/login")
email=driver.find_element(By.ID,"Email")
email.send_keys("abc@gmail.com")
time.sleep(3)
print(email.text)
print(email.get_attribute("value"))