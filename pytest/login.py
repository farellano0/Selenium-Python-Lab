import os
import sys

current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..', 'funciones'))
sys.path.insert(0, parent_dir)

import pytest
from Funciones import FuncionesGlobales
from login_Page import Login_Page

global driver
global funciones
funciones = FuncionesGlobales()
funciones.init()
driver = funciones.driver
login = Login_Page(driver)
t= 1

# Credenciales incorrectas
def test_login1():
    login.Login_Master("admin@yourstore.com", "123456")
    funciones.existe("xpath","//h3[contains(.,'Epic sadface: Username and password do not match any user in this service')]",t)
    
# Campos vacíos
def test_login2():
    funciones.navegar("https://www.saucedemo.com/")
    funciones.click_valida("id", "login-button", t)
    funciones.existe("xpath","//h3[@data-test='error'][contains(.,'Epic sadface: Username is required')]",t)
    
# Campos llenados incorrectamente
def test_login3():
    login.Login_Master("fernando", "secret_sauce")
    funciones.existe("xpath","//h3[@data-test='error'][contains(.,'Epic sadface: Username and password do not match any user in this service')]",t)
    
# Happy Path
def test_login4():
    login.Login_Master("standard_user", "secret_sauce")
    funciones.existe("xpath","//div[@class='app_logo'][contains(.,'Swag Labs')]",t)