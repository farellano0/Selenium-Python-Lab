import os
import sys
import pytest
import allure

# Ruta para importar módulos desde la carpeta 'funciones'
current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..', 'funciones'))
sys.path.insert(0, parent_dir)

from Funciones import FuncionesGlobales
from login_Page import Login_Page
from allure_commons.types import AttachmentType


# Tiempo de espera para verificaciones en la UI
WAIT_TIME = 1

@pytest.fixture()
def log_on_failure(request, setup_login_dos):
    yield
    funciones = setup_login_dos
    driver = funciones.driver
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="Error", attachment_type=AttachmentType.PNG)

@pytest.fixture(scope='function')
def setup_login_uno():
    """
    Fixture para inicializar el driver y la clase FuncionesGlobales.
    """
    funciones = FuncionesGlobales()
    funciones.init()
    driver = funciones.driver
    login = Login_Page(driver)

    # Iniciar prueba
    print("\n--- INICIO DE LA PRUEBA UNO ---")
    login.Login_Master("standard_user", "secret_sauce")
    print("Entrando al sistema uno")

    # Verificar que el elemento de productos existe
    funciones.existe("xpath", "//span[@class='title'][contains(.,'Products')]", WAIT_TIME)
    
    # Devolver el driver y funciones para su uso en la prueba
    yield funciones

    # Cerrar el navegador al finalizar la prueba
    print("\nSalida del login uno")
    driver.quit()

@pytest.fixture(scope='function')
def setup_login_dos():
    """
    Fixture para inicializar el driver y la clase FuncionesGlobales.
    """
    funciones = FuncionesGlobales()
    funciones.init()
    driver = funciones.driver

    # Iniciar prueba
    print("\n--- INICIO DE LA PRUEBA DOS ---")
    
    # Navegar a la URL de la aplicación
    funciones.navegar("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Validar que los campos de usuario y contraseña se llenen correctamente
    funciones.validar_texto("xpath", "//input[contains(@name,'username')]", "Admin", WAIT_TIME)
    funciones.validar_texto("xpath", "//input[contains(@type,'password')]", "admin123", WAIT_TIME)

    # Realizar login
    funciones.click_valida("xpath", "//button[@type='submit'][contains(.,'Login')]", WAIT_TIME)
    print("Entrando al sistema dos")
    
    # Verificar que el dashboard exista
    funciones.existe("xpath", "//h6[contains(.,'Dashboard')]", WAIT_TIME)
    
    # Devolver el driver y funciones para su uso en la prueba
    yield funciones

    # Cerrar el navegador al finalizar la prueba
    print("\nSalida del login dos")
    driver.quit()

# Pruebas
@pytest.mark.usefixtures("log_on_failure")
def test_uno(setup_login_uno):
    """
    Prueba que utiliza el login en el sistema uno.
    """
    print("Realizando acciones adicionales en el sistema uno")

@pytest.mark.usefixtures("log_on_failure")
def test_dos(setup_login_dos):
    """
    Prueba que utiliza el login en el sistema dos.
    """
    funciones = setup_login_dos
    funciones.click_valida("xpath", "//span[contains(.,'My Info')]", WAIT_TIME)
    funciones.validar_texto("xpath", "//input[@name='firstName']", "Fernando", WAIT_TIME)
    funciones.validar_texto("xpath", "//input[@name='middleName']", "Arellano", WAIT_TIME)
    funciones.validar_texto("xpath", "//input[@name='lastName']", "Velasco", WAIT_TIME)
    funciones.click_valida("xpath", "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button", WAIT_TIME)
    element = funciones._find_element("xpath", "//input[@name='firstName']").get_attribute("value")
    
    assert element == "Fernanda", "El nombre no coincide"
