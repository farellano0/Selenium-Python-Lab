from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\\Drivers\\chromedriver.exe"
s = Service(PATH)
driver = webdriver.Chrome(service = s)

driver.get("http://demoqa.com/text-box")
print("Bienvenido a Selenium")
print(driver.title)

driver.close()