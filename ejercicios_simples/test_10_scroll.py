from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

PATH = "C:\\Drivers\\chromedriver.exe"
s = Service(PATH)
driver = webdriver.Chrome(service = s)
t = 2

driver.get("https://pixabay.com/es/")
driver.maximize_window()
driver.implicitly_wait(15)
time.sleep(t)

try:
    # Aceptar cookies
    cookies = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@id='onetrust-accept-btn-handler']")))
    cookies = driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
    cookies.click()

    # Esperar y desplazar el botón "Descubre más" a la vista
    Buscar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Búsquedas populares')]")))
    Buscar = driver.find_element(By.XPATH, "//span[contains(text(),'Búsquedas populares')]")
    driver.execute_script("arguments[0].scrollIntoView(true);", Buscar)
    time.sleep(t)
    
    # Intentar hacer clic varias veces si es necesario
    clicked = False
    attempts = 0
    while not clicked and attempts < 5:
        try:
            Buscar.click()
            clicked = True
        except Exception as e:
            print(f"Intento {attempts+1} fallido: {str(e)}")
            time.sleep(t)
            attempts += 1

except TimeoutException as ex:
    print(ex.msg)
    print("Error de TimeoutException")

time.sleep(t)
driver.close()
