import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='dob']").click()
time.sleep(4)
moth_Picker=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
moth_Picker.select_by_visible_text("Apr")
year_Picker=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
year_Picker.select_by_visible_text("2017")
time.sleep(2)
dates=driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']//table/tbody/tr/td/a")
for date in dates:

    if date.text=="10":
        date.click()
        break;
time.sleep(3)


