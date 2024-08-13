from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

PATH = "C:\\Drivers\\chromedriver.exe"
s = Service(PATH)
driver = webdriver.Chrome(service = s)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)

nom = driver.find_element(By.XPATH, "//input[@id='userName']")
email = driver.find_element(By.XPATH, "//input[@id='userEmail']")
currentAddress = driver.find_element(By.XPATH, "//textarea[@id='currentAddress']")
permantAddress = driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']")
btnSubmit = driver.find_element(By.XPATH, "//button[@id='submit']")


nom.send_keys("Fernando")
email.send_keys("farellano0@gmail.com")
currentAddress.send_keys("Dirección uno.")
permantAddress.send_keys("Dirección dos")
time.sleep(1)

driver.execute_script("window.scrollTo(0,500)")
time.sleep(2)

btnSubmit.click()


time.sleep(5)

driver.close()