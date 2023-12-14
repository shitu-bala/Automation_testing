import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()
clicklink=Keys.CONTROL+Keys.ENTER
driver.find_element(By.LINK_TEXT,"Register").send_keys(clicklink)
time.sleep(3)
