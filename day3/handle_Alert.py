from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
time.sleep(5)
alertbox = driver.switch_to.alert
alertbox.send_keys("welcome")
time.sleep(3)
alertbox.accept()
time.sleep(3)
