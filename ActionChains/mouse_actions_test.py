import os
import sys
parent = os.path.abspath('.')
sys.path.insert(1, parent)

import unittest
from funciones.Funciones import FuncionesGlobales

t = 3

class BaseTest(unittest.TestCase):

    def setUp(self):
        print("\n--- Iniciando prueba ---")
        self.funciones = FuncionesGlobales()
        self.funciones.init()
        self.driver = self.funciones.driver

    def test1(self):
        print("\nEjecutando test: Doble clic en Demo QA")
        self.funciones.navegar("https://demoqa.com/buttons")
        self.funciones.doble_click("xpath", "//button[contains(@id,'doubleClickBtn')]", t)
        resultado = self.funciones.existe("xpath", "//p[contains(@id,'doubleClickMessage')]", t)
        self.assertEqual(resultado, "Existe", "El mensaje de doble clic no apareció")
        print("Test1 completado")

    def tearDown(self):
        print("\n--- Finalizando prueba ---")
        self.funciones.salida()

if __name__ == "__main__":
    unittest.main(verbosity=2)