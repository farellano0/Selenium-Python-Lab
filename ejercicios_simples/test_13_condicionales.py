from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Configuración del driver de Chrome
CHROME_DRIVER_PATH = "C:\\Drivers\\chromedriver.exe"
SERVICE = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=SERVICE)

# Configuración de tiempos de espera
IMPLICIT_WAIT_TIME = 15
EXPLICIT_WAIT_TIME = 5
ACTION_WAIT_TIME = 2

driver.implicitly_wait(IMPLICIT_WAIT_TIME)

# Navegar a la página web de ejemplo y maximizar la ventana
driver.get("https://demoqa.com/text-box")
driver.maximize_window()

def check_element_visibility(xpath, element_name):
    try:
        element = WebDriverWait(driver, EXPLICIT_WAIT_TIME).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        is_displayed = element.is_displayed()
        print(f"{element_name} is displayed: {is_displayed}")
    except TimeoutException:
        print(f"Error: TimeOut Exception for {element_name}")

def check_element_enabled(xpath, element_name):
    try:
        element = WebDriverWait(driver, EXPLICIT_WAIT_TIME).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        is_enabled = element.is_enabled()
        print(f"{element_name} is enabled: {is_enabled}")
    except TimeoutException:
        print(f"Error: TimeOut Exception for {element_name}")

# Verificar visibilidad de la imagen
check_element_visibility("//img[@src='/images/Toolsqa.jpg']", "Image")

# Verificar si el botón está habilitado
check_element_enabled("//button[@id='submit']", "Submit Button")

# Esperar antes de cerrar el navegador
time.sleep(ACTION_WAIT_TIME)
driver.quit()
