import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj = Service("C:\webdrivers\chromedriver.exe")

driver = webdriver.Chrome(service= serv_obj)
driver.get("https://www.flipkart.com/")
driver.get("https://www.amazon.ca/")
time.sleep(2)
driver.back()
time.sleep(2)
#driver.refresh
driver.forward()
