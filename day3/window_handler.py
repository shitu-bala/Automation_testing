
import time

import requests
from requests import request
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
windowIDs= driver.window_handles
parentwindowID=windowIDs[0]
childwindowID=windowIDs[1]
#driver.switch_to.window(childwindowID)
#driver.find_element(By.XPATH,"//input[@id='Form_submitForm_EmailHomePage']").send_keys("abc@gmail.com")

#time.sleep(4)
#driver.switch_to.window(parentwindowID)
#driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("xyz@hot.com")
for wind in windowIDs:
    driver.switch_to.window(wind)
    if driver.title=="OrangeHRM":
     driver.close()
time.sleep(4)



