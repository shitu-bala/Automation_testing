import time

import requests
from requests import request
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
opt= Options()
opt.add_argument("--disable notifications")
driver = webdriver.Chrome()
driver.get("https://whatmylocation.com/")

