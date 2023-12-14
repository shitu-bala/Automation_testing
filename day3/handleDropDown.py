import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(5)
country_ele = driver.find_element(By.XPATH, "//select[@id='country']")

time.sleep(3)
country = Select(country_ele)
country.select_by_visible_text("India")
time.sleep(5)

