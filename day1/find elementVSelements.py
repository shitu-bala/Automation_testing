import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj = Service("C:\webdrivers\chromedriver.exe")

driver = webdriver.Chrome(service= serv_obj)
driver.get("https://demo.nopcommerce.com/")
#elements= driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
elements= driver.find_elements(By.XPATH,"//div[@class='footer']//a")
for element in elements:
    print(element.text)
elements[1].click()
time.sleep(4)
print(len(elements))