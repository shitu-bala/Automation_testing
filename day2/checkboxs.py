import time

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()
time.sleep(2)
#driver.find_element(By.XPATH,"//label[normalize-space()='Monday']").click()
checkboxs =driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")

#print(len(checkboxs))
#for checkbox in checkboxs:
    #checkbox.click()
for i in range(len(checkboxs)-2,len(checkboxs)):
    checkboxs[i].click()



time.sleep(5)
