import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.yatra.com/")
driver.maximize_window()
time.sleep(2)
account=driver.find_element(By.XPATH,"//a[contains(text(),'My Account')]")
time.sleep(2)
login=driver.find_element(By.XPATH,"//a[@id='signInBtn']")
ac=ActionChains(driver)
ac.move_to_element(account).move_to_element(login).click().perform()
time.sleep(5)