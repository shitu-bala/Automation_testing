
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.save_screenshot("C:\\Users\\Arun\\PycharmProjects\\Automation_testing\\day6\\sreenshot.png")