
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome()

mywaits = WebDriverWait(driver,10,poll_frequency= 2 ,ignored_exceptions= Exception)

driver.get("https://www.google.com/")
driver.maximize_window()

searchBox= driver.find_element(By.CLASS_NAME,"gLFyf")
searchBox.send_keys("selenium")
searchBox.submit()
seachlink = mywaits.until(EC.presence_of_element_located((By.XPATH,"//h3[normalize-space()='Selenium']")))
seachlink.click()


