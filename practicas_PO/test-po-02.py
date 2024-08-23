import os, sys
parent = os.path.abspath('.')
sys.path.insert(1, parent)

import unittest
from funciones.Funciones import FuncionesGlobales
from funciones.login_Page import Login_Page

t= 1

class base_test(unittest.TestCase):

    def setUp(self):
        print("\n--- Iniciando prueba ---")
        self.funciones = FuncionesGlobales()
        self.funciones.init()
        self.driver = self.funciones.driver
        self.funcionesLP = Login_Page(self.driver)

    def test1(self):
        print("\nEjecutando test")
        self.funcionesLP.Login_Master("standard_user", "secret_sauce")
        

    def tearDown(self):
        print("\n--- Finalizando prueba ---")
        self.funciones.salida()
        
if __name__ == "__main__":
    unittest.main()