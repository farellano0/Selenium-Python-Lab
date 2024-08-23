import os, sys
parent = os.path.abspath('.')
sys.path.insert(1, parent)

import unittest
from funciones.Funciones import FuncionesGlobales

t= 1


class BaseTest(unittest.TestCase):
    def setUp(self):
        print("\n--- Iniciando prueba ---")
        self.funciones = FuncionesGlobales()
        self.funciones.init()
        self.driver = self.funciones.driver

    def test1(self):
        print("\nEjecutando test1: Inicio de sesión en Sauce Demo")
        self.funciones.navegar("https://www.saucedemo.com/")
        self.funciones.validar_texto("xpath", "//input[contains(@id,'user-name')]", "Fernando", t)
        self.funciones.validar_texto("xpath", "//input[@id='password']", "secret_sauce", t)
        self.funciones.click_valida("xpath", "//input[@id='login-button']", t)
        print("Test1 completado")

    def tearDown(self):
        print("\n--- Finalizando prueba ---")
        self.funciones.salida()

if __name__ == "__main__":
    unittest.main(verbosity=2)