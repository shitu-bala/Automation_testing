import time

from selenium import webdriver
from  selenium.webdriver.common.by import By
import os
location=os.getcwd()
def Chrom_setup():
    prefrences={"download.default_directory": location}
    oops=webdriver.ChromeOptions()
    oops.add_experimental_option("prefs",prefrences)
    driver= webdriver.Chrome(options=oops)

    return driver
driver=Chrom_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()
driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()
time.sleep(6)