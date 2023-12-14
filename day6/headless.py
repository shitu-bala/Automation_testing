
from selenium import webdriver
from selenium.webdriver.common.by import By
def headless_chrome():
    ops=webdriver.ChromeOptions()

    driver=webdriver.Chrome(options=ops)
    ops.headless=True
    return driver
driver= headless_Edge()
def headless_chrome():
    ops=webdriver.EdgeOptions()

    driver=webdriver.Edge(options=ops)
    ops.headless=True
    return driver


driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)