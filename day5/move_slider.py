import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.nationsonline.org/oneworld/countries_of_the_world.htm")
driver.execute_script("window.scrollBy(0,3000)","")
time.sleep(5)
driver.execute_script("return window.pageYoffset")