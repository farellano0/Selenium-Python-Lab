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
        print("\nEjecutando test: Drag and Drop en Demo QA")
        self.funciones.navegar("https://www.google.com/")
        self.funciones.validar_texto("xpath", "//textarea[contains(@id,'APjFqb')]", "fer", t)
        self.funciones.click_xy("xpath", "//textarea[contains(@id,'APjFqb')]", 0, 250, t)
        print("Test completado")
        

    def tearDown(self):
        print("\n--- Finalizando prueba ---")
        self.funciones.salida()

if __name__ == "__main__":
    unittest.main(verbosity=2)