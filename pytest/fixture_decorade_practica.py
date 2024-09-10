import os
import sys
import pytest

# Ruta para importar módulos desde la carpeta 'funciones'
current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..', 'funciones'))
sys.path.insert(0, parent_dir)

from Funciones import FuncionesGlobales
from login_Page import Login_Page


# Tiempo de espera para verificaciones en la UI
WAIT_TIME = 1

@pytest.fixture(scope='function')
def setup_login_uno():
    """
    Fixture para inicializar el driver y realizar el login en la primera aplicación.
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
    
    # Devolver el driver para su uso en la prueba
    yield driver

    # Cerrar el navegador al finalizar la prueba
    print("\nSalida del login uno")
    driver.quit()

@pytest.fixture(scope='function')
def setup_login_dos():
    """
    Fixture para inicializar el driver y realizar el login en la segunda aplicación.
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
    
    # Devolver el driver para su uso en la prueba
    yield driver

    # Cerrar el navegador al finalizar la prueba
    print("\nSalida del login dos")
    driver.quit()

@pytest.mark.usefixtures("setup_login_uno")
def test_uno():
    """
    Prueba que utiliza el login en el sistema uno.
    """
    print("Realizando acciones adicionales en el sistema uno")

@pytest.mark.usefixtures("setup_login_dos")
def test_dos():
    """
    Prueba que utiliza el login en el sistema dos.
    """
    print("Realizando acciones adicionales en el sistema dos")
