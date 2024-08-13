from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

PATH = "C:\\Drivers\\chromedriver.exe"
s = Service(PATH)
driver = webdriver.Chrome(service = s)
t = 1

driver.get("https://seleniumeasy.com/test/basic-first-fomr-demo.html")
driver.maximize_window()
t=3

time.sleep(5)
driver.close()