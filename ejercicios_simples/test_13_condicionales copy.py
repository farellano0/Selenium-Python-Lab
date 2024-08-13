from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging
import time

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constantes de configuración
CHROME_DRIVER_PATH = "C:\\Drivers\\chromedriver.exe"
IMPLICIT_WAIT_TIME = 15
EXPLICIT_WAIT_TIME = 5
ACTION_WAIT_TIME = 2
URL = "https://demoqa.com/text-box"

class WebDriverSetup:
    def __init__(self, driver_path):
        self.service = Service(driver_path)
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.implicitly_wait(IMPLICIT_WAIT_TIME)
    
    def navigate_to_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        logging.info(f"Navigated to {url}")
    
    def quit_driver(self):
        self.driver.quit()
        logging.info("Driver quit successfully")

class ElementChecker:
    def __init__(self, driver):
        self.driver = driver
    
    def check_element_visibility(self, xpath, element_name):
        try:
            element = WebDriverWait(self.driver, EXPLICIT_WAIT_TIME).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            is_displayed = element.is_displayed()
            logging.info(f"{element_name} is displayed: {is_displayed}")
            return is_displayed
        except TimeoutException:
            logging.error(f"Error: TimeOut Exception for {element_name}")
            return False

    def check_element_enabled(self, xpath, element_name):
        try:
            element = WebDriverWait(self.driver, EXPLICIT_WAIT_TIME).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            is_enabled = element.is_enabled()
            logging.info(f"{element_name} is enabled: {is_enabled}")
            return is_enabled
        except TimeoutException:
            logging.error(f"Error: TimeOut Exception for {element_name}")
            return False

def main():
    web_driver_setup = WebDriverSetup(CHROME_DRIVER_PATH)
    web_driver_setup.navigate_to_url(URL)

    element_checker = ElementChecker(web_driver_setup.driver)

    # Verificar visibilidad de la imagen
    element_checker.check_element_visibility("//img[@src='/images/Toolsqa.jpg']", "Image")

    # Verificar si el botón está habilitado
    element_checker.check_element_enabled("//button[@id='submit']", "Submit Button")

    # Esperar antes de cerrar el navegador
    time.sleep(ACTION_WAIT_TIME)
    web_driver_setup.quit_driver()

if __name__ == "__main__":
    main()
