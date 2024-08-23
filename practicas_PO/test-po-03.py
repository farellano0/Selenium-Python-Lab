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
        print("\nEjecutando test")
        self.funciones.navegar("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
        self.funciones.select_type("xpath", "//select[@id='select-demo']", "value", "Sunday", t)
        self.funciones.select_type("xpath","//select[@id='select-demo']", "text", "Wednesday", t)
        self.funciones.select_type("xpath","//select[@id='select-demo']", "index", "6", t)
        print("Test completado")

    def tearDown(self):
        print("\n--- Finalizando prueba ---")
        self.funciones.salida()
        
if __name__ == "__main__":
    unittest.main(verbosity=2)