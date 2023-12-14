import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
serv_obj = Service("C:\webdrivers\chromedriver.exe")

driver = webdriver.Chrome(service= serv_obj)
driver.get("https://www.orangehrm.com/")
time.sleep(5)

links = driver.find_element(By.LINK_TEXT,"Executive Profile").click()




time.sleep(4)


