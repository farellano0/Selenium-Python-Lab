from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

PATH = "C:\\Drivers\\chromedriver.exe"
s = Service(PATH)
driver = webdriver.Chrome(service = s)
t=1

driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(t)

daySelect = driver.find_element(By.XPATH, "//select[@id='select-demo']")
dSelector = Select(daySelect)

dSelector.select_by_visible_text("Sunday")
time.sleep(t)

dSelector.select_by_index(3)
time.sleep(t)

dSelector.select_by_value("Saturday")
time.sleep(t)

# Otra forma de hacer los select
driver.execute_script("window.scrollTo(0,500)")
ciudadSelect = Select(driver.find_element(By.XPATH, "//select[@id='multi-select']"))
btnFSelected = driver.find_element(By.XPATH, "//button[@id='printMe']")
btnGASelected = driver.find_element(By.XPATH, "//button[@id='printAll']")

ciudadSelect.select_by_visible_text("Texas")
btnFSelected.click()
time.sleep(t)

ciudadSelect.select_by_index(2)
btnGASelected.click()
time.sleep(t)

ciudadSelect.select_by_value("Washington")
btnFSelected.click()
time.sleep(t)

driver.close()
