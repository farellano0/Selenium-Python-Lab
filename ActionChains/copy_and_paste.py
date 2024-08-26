import os
import sys
parent = os.path.abspath('.')
sys.path.insert(1, parent)

import unittest
from funciones.Funciones import FuncionesGlobales
from selenium.webdriver.common.action_chains import ActionChains

t = 2

class BaseTest(unittest.TestCase):

    def setUp(self):
        print("\n--- Iniciando prueba ---")
        self.funciones = FuncionesGlobales()
        self.funciones.init()
        self.driver = self.funciones.driver

    def test1(self):
        print("\nEjecutando test: Drag and Drop en Demo QA")
        self.funciones.navegar("https://demoqa.com/automation-practice-form")
        
        self.funciones.validar_texto("xpath", "//input[contains(@id,'firstName')]", "Juan", t)
        
        actions = ActionChains(self.driver)
        actions.key_down(self.funciones.key('control')).send_keys('a').send_keys('c').key_up(self.funciones.key('control')).perform()
        self.funciones.tiempo(t)
        actions.send_keys(self.funciones.key('tab'))
        actions.key_down(self.funciones.key('control')).send_keys('v').key_up(self.funciones.key('control')).perform()
        actions.send_keys(self.funciones.key('tab'))
        
        self.funciones.tiempo(t)
        print("Test completado")

    def tearDown(self):
        print("\n--- Finalizando prueba ---")
        self.funciones.salida()

if __name__ == "__main__":
    unittest.main(verbosity=2)