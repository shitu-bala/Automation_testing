import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
driver.switch_to.frame(0)
#driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("7/30/2023")
month="November"
year= "2023"
date= "24"
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
while True:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mon==month and yr==year:
        break;

    else:
        driver.find_element(By.XPATH,"//a[@title='Next']").click()

time.sleep(3)
dates=driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']//table/tbody/tr/td/a")
for ele in dates:
    if ele.text==date:
        ele.click()
        break;



time.sleep(5)




