import time

import requests
from requests import request
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
driver.switch_to.frame("mce_0_ifr")
time.sleep(4)
driver.find_element(By.ID,"tinymce").send_keys("hello welcome")
time.sleep(4)