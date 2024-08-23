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
        print("\nEjecutando test: Checkbox en Demo QA")
        self.funciones.navegar("https://demoqa.com/checkbox")
        self.funciones.check("xpath", "//button[contains(@aria-label,'Toggle')]", t)
        self.funciones.check("xpath", "//label[@for='tree-node-documents'][contains(.,'Documents')]", t)
        self.funciones.check("xpath", "//label[@for='tree-node-downloads'][contains(.,'Downloads')]", t)
        print("Test1 completado")

    def tearDown(self):
        print("\n--- Finalizando prueba ---")
        self.funciones.salida()

if __name__ == "__main__":
    unittest.main(verbosity=2)