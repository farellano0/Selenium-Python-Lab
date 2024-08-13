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
driver.get("https://demo.seleniumeasy.com/javascript-alert-box-demo.html")
driver.maximize_window()

try:
    # Encontrar y hacer clic en el botón de alerta simple
    alert_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-default'][contains(.,'Click me!')]"))
    )
    alert_button.click()
    time.sleep(t)
    
    # Aceptar la alerta
    driver.switch_to.alert.accept()
    
    # Encontrar y hacer clic en el botón de alerta de confirmación
    confirm_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-default btn-lg'][contains(.,'Click me!')]"))
    )
    confirm_button.click()
    time.sleep(t)
    
    # Cancelar la alerta de confirmación
    driver.switch_to.alert.dismiss()
    print("Alerta de confirmación cancelada.")
    
    # Verificar que el mensaje de cancelación se muestra
    result_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[@id='confirm-demo']"))
    )
    assert result_message.is_displayed() and result_message.text == "You pressed Cancel!"

except TimeoutException as ex:
    print("TimeoutException: ", ex.msg)
    print("Error: No se pudo encontrar el elemento en el tiempo especificado.")
except NoAlertPresentException as ex:
    print("NoAlertPresentException: ", ex.msg)
    print("Error: No se encontró la alerta esperada.")
except AssertionError as ex:
    print("AssertionError: ", ex)
    print("Error: La condición assert no se cumplió.")
finally:
    # Esperar un tiempo antes de cerrar el navegador
    time.sleep(t)
    driver.close()
    print("Navegador cerrado.")
