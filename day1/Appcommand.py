import time
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj = Service("C:\webdrivers\chromedriver.exe")

driver = webdriver.Chrome(service= serv_obj)
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
seachbox= driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("Displayed result :" , seachbox.is_displayed())
print("Enabled status : ",seachbox.is_enabled())
time.sleep(3)
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
rb_female = driver.find_element(By.XPATH,"//input[@id='gender-female']")
print(rb_female.is_selected())
time.sleep(2)
rb_female.click()
print(rb_female.is_selected())



#print(driver.page_source)