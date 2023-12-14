import time

import requests
from requests import request
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
links= driver.find_elements(By.TAG_NAME,"a")
count=0
for link in links:
    url= link.get_attribute("href")
    try:
     resp=requests.head(url)
    except:
        None

    if resp.status_code>=400:
        print( url , " this is broken link ")
        count+=1
    else:
        print(url ," this is valid link" )
print("Total broken links ", count)





