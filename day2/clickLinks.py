
driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()
links= driver.find_elements(By.TAG_NAME,"a")
print("Total number of links :" ,len(links))
time.sleep(4)