from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\\Drivers\\chromedriver.exe"
s = Service(PATH)
driver = webdriver.Chrome(service = s)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(3)

driver.get("https://www.finpo.com.mx/contacto.php#")
time.sleep(3)

driver.get("https://www.youtube.com/")
time.sleep(3)

driver.execute_script("window.history.go(-1)")
time.sleep(3)

driver.execute_script("window.history.go(-1)")
time.sleep(3)

# driver.forward()
driver.execute_script("window.history.go(2)")
time.sleep(3)

driver.close()