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
        self.funciones.navegar("https://demoqa.com/dragabble")
        self.funciones.drag_and_drop("xpath", "//div[contains(@id,'dragBox')]", "//h1[@class='text-center'][contains(.,'Dragabble')]", t)
        print("Test completado")
        self.funciones.tiempo(5)

    def tearDown(self):
        print("\n--- Finalizando prueba ---")
        self.funciones.salida()

if __name__ == "__main__":
    unittest.main(verbosity=2)