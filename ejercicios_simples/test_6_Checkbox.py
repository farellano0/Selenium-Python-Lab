from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\\Drivers\\chromedriver.exe"
s = Service(PATH)
driver = webdriver.Chrome(service = s)
t=3

driver.get("https://demo.seleniumeasy.com/basic-checkbox-demo.html")
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(t)

btn1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@type,'checkbox')])[1]")))
btn1.click()

driver.execute_script("window.scrollTo(0, 300)")

time.sleep(t)

btn2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@type,'checkbox')])[4]")))
btn2.click()

btn3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@type,'checkbox')])[6]")))
btn3.click()

btn4 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//input[contains(@type,'checkbox')])[7]")))
btn4.click()

time.sleep(3)
driver.close()