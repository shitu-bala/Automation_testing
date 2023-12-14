import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver import  ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://text-compare.com/")
driver.maximize_window()
input1=driver.find_element(By.ID,"inputText1")
input2=driver.find_element(By.ID,"inputText2")
input1.send_keys("welcome to python")

act= ActionChains(driver)
time.sleep(2)
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
time.sleep(2)
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
time.sleep(2)
act.send_keys(Keys.TAB).perform()
time.sleep(2)
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(3)



