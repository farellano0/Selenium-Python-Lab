import os
import sys
import pytest
import allure

# Ruta para importar módulos desde la carpeta 'funciones'
current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..', 'funciones'))
sys.path.insert(0, parent_dir)

from Funciones import FuncionesGlobales
from allure_commons.types import AttachmentType
from login_Page import Login_Page


# Tiempo de espera para verificaciones en la UI
WAIT_TIME = 1

@pytest.fixture(scope="module")
def setup_login():
    global funciones
    global driver
    funciones = FuncionesGlobales()
    funciones.init()
    driver = funciones.driver
    print("\n--- INICIO DE LA PRUEBA ---")
    funciones.navegar("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    funciones.validar_texto("xpath", "//input[contains(@name,'username')]", "Admin", WAIT_TIME)
    funciones.validar_texto("xpath", "//input[contains(@type,'password')]", "admin123", WAIT_TIME)
    funciones.click_valida("xpath", "//button[@type='submit'][contains(.,'Login')]", WAIT_TIME)
    
    yield driver

    print("\nSalida de la prueba")
    driver.quit()
    
def test_uno(setup_login):
    etiqueta = funciones.existe("xpath", "//h6[contains(.,'Dashboard')]", WAIT_TIME)
    allure.attach(driver.get_screenshot_as_png(), name="Sesión iniciada", attachment_type=AttachmentType.PNG)
    if etiqueta:
        assert True, "Se hizo el login correctamente."
    else:
        assert False, "No se realizó el login correctamente."
