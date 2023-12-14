import time


from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
NoOfRows=len(driver.find_elements(By.XPATH,"(//table[@name='BookTable'])//tr"))

NoOfColumns=len(driver.find_elements(By.XPATH,"(//table[@name='BookTable'])//tr[1]/th"))
print(NoOfColumns)

print(NoOfRows)
#value= driver.find_element(By.XPATH,"(//table[@name='BookTable'])/tbody/tr[4]/td[2]").text
#print(value)

for r in range(2,NoOfRows+1):
    for c in range(1,NoOfRows+1):
        data= driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+")]").text
        print(data)


