import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from day7 import utility

driver= webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india/fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.maximize_window()

time.sleep(2)
file="C:\Automation Testing\InrestData.xlsx"
#workbook=openpyxl.load_workbook(file)
#Sheet1=workbook["Sheet1"]

rows=utility.GetRowCount(file,"Sheet1")
print(rows)
for r in range(2,rows+1):
    princ=utility.ReadData(file,"Sheet1",r,1)
    rateofInterest= utility.ReadData(file,"Sheet1",r,2)
    per1=utility.ReadData(file,"Sheet1",r,3)
    per2=utility.ReadData(file,"Sheet1",r,4)
    freq= utility.ReadData(file,"Sheet1",r,5)
    expeted_mvalue=utility.ReadData(file,"Sheet1",r,6)
    print(per2)
    driver.find_element(By.ID,"principal").send_keys(princ)
    driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(rateofInterest)
    driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(per1)
    timedrp=Select(driver.find_element(By.XPATH,"(//select[@id='tenurePeriod'])[1]"))
    timedrp.select_by_visible_text(per2)
    freqdrp=Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
    freqdrp.select_by_visible_text(freq)
    driver.find_element(By.XPATH,"//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']").click()
    actualMvalue=driver.find_element(By.XPATH,"(//span[@id='resp_matval'])[1]").text
    print(actualMvalue)
    if float(expeted_mvalue)==float(actualMvalue):
        print("Test Passed")
        utility.WriteData(file,"Sheet1",r,8,"passed")
        utility.FillGreenColor(file,"Sheet1",r,8)
    else:
        print("Test failed")
        utility.WriteData(file, "Sheet1", r, 8, "failed")
        utility.FillRedColor(file, "Sheet1", r, 8)
    driver.find_element(By.XPATH,"//img[@class='PL5']").click()
    time.sleep(2)

driver.close()


    