from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://money.rediff.com/index.html")
#text1_data = driver.find_element(By.XPATH,"//a[normalize-space()='Tata Consultancy']/parent::li").
text1_data = driver.find_elements(By.XPATH,"//a[normalize-space()='Tata Consultancy']/ancestor::ul/child::li")


print(len(text1_data))

