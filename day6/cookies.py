
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
cookies= driver.get_cookies()
print("size of cookies  :", len(cookies))
for c in cookies:
    #print(c)
     print(c.get('value'),":",c.get('name'))
