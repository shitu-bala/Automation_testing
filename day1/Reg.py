import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://demo.opencart.com/index.php?route=account/register")

driver.maximize_window()
driver.execute_script('document.getElementsByTagName("html")[0].style.scrollBehavior="auto"')
#driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[@id='input-firstname']").send_keys("chbnggdu")
driver.find_element(By.XPATH,"//input[@id='input-lastname']").send_keys("bradhhbhjj")
driver.find_element(By.XPATH,"//input[@id='input-email']").send_keys("dotgtc1csg6gg221@gyxmz.com")
driver.find_element(By.XPATH,"//input[@id='input-password']").send_keys("aanbhhgtyu@1234")
#time.sleep(7)
driver.find_element(By.XPATH,"//input[@name='agree']").click()
#time.sleep(5)
#driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
time.sleep(5)

#driver.find_element(By.XPATH,"//a[normalize-space()='Your Account Has Been Created!']").text



