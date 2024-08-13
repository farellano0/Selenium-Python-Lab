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
time.sleep(2)

nom = driver.find_element(By.XPATH, "//input[@id='userName' and @type='text']")
nom.send_keys("Fernando")
nom.send_keys(Keys.TAB + "farellano@gmail.com" + Keys.TAB + "Dirección uno" + Keys.TAB + "Dirección dos" + Keys.TAB + Keys.ENTER)
time.sleep(5)

driver.close()