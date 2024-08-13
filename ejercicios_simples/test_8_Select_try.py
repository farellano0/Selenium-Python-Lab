from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import time

PATH = "C:\\Drivers\\chromedriver.exe"
s = Service(PATH)
driver = webdriver.Chrome(service = s)
t=1

driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
driver.maximize_window()
time.sleep(t)

try:
    daySelect = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "//select[@id='select-demo']")))
    dSelector = Select(daySelect)

    dSelector.select_by_visible_text("Sunday")
    time.sleep(t)

    dSelector.select_by_index(3)
    time.sleep(t)

    dSelector.select_by_value("Saturday")
    time.sleep(t)
except TimeoutException as ex: 
    print(ex.msg)
    print("El elemento no está disponible.")

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
