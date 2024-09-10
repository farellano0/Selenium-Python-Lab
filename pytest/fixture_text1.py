import os
import sys

current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..', 'funciones'))
sys.path.insert(0, parent_dir)

import pytest
from Funciones import FuncionesGlobales

t= 1

def setup_function(function):
    global driver
    global funciones
    funciones = FuncionesGlobales()
    funciones.init()
    driver = funciones.driver
    print("\n--- INCIO DE LA PRUEBA ---")
    funciones.navegar("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
    
def teardown_function(function):
    print("\n--- FIN DE LA PRUEBA ---")
    driver.close()

def test_uno():
    funciones.validar_texto("id", "Email", "admin@yourstore.com", t)
    funciones.validar_texto("id", "Password", "admin", t)
    funciones.click_valida("xpath", "//button[@type='submit'][contains(.,'Log in')]", t)
    
def test_dos():
    print("Hola Mundo")
    funciones.tiempo(5)