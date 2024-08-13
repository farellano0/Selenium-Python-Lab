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
t=2

driver.get("https://testpages.herokuapp.com/styled/file-upload-test.html")
driver.maximize_window()
driver.implicitly_wait(15)
time.sleep(t)

try:
    fileInput = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@id='fileinput']")))
    fileInput = driver.find_element(By.XPATH, "//input[@id='fileinput']")
    fileInput.send_keys("C:\\Users\\Fer Arellano\\Documents\\Selenium\\Curso\\images\\ice-cream-8195933_640.png")

    driver.find_element(By.XPATH, "//input[@id='itsanimage']").click()
    driver.find_element(By.XPATH, "//input[@type='submit']").click()

    resultado = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//p[contains(.,'ice-cream-8195933_640.png')]")))
    resultado = driver.find_element(By.XPATH, "//p[contains(.,'ice-cream-8195933_640.png')]")
    resultado = resultado.is_displayed()
    print(resultado)

except TimeoutException as ex:
    print(ex.msg)
    print("Fail")

time.sleep(t)
driver.close()