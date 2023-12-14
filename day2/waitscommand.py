from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj = Service("C:\webdrivers\chromedriver.exe")

driver = webdriver.Chrome(service= serv_obj)
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
driver.maximize_window()

searchBox= driver.find_element(By.CLASS_NAME,"gLFyf")
searchBox.send_keys("selenium")
searchBox.submit()
driver.find_element(By.XPATH,"//h3[normalize-space()='Selenium']").click()

