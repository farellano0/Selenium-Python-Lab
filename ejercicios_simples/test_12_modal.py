from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoAlertPresentException
import time

# Ruta del driver de Chrome
PATH = "C:\\Drivers\\chromedriver.exe"
s = Service(PATH)
driver = webdriver.Chrome(service=s)

# Tiempo de espera implícita para encontrar elementos
driver.implicitly_wait(15)

# Tiempo de espera entre acciones
t = 2

# Navegar a la página web de ejemplo
driver.get("https://demo.seleniumeasy.com/bootstrap-modal-demo.html")
driver.maximize_window()

# Single Modal Example
modal = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='#myModal0']")))
modal.click()

try:
    btnSave = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "(//a[@href='#'][contains(.,'Save changes')])[1]")))
    btnSave.click()

except TimeoutException as ex:
    print(ex.msg)
    print('Error: TimeoutException')

# Multiple Modal Example
modal = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='#myModal']")))
modal.click()

try:
    secondModal = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='#myModal2']")))
    secondModal.click()

    btnSave = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "(//a[@href='#'][contains(.,'Save changes')])[3]")))
    btnSave.click()

except TimeoutException as ex:
    print(ex.msg)
    print('Error: TimeoutException')

time.sleep(t)
driver.close()