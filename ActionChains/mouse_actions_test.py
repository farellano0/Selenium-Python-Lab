import os, sys
parent = os.path.abspath('.')
sys.path.insert(1, parent)

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from funciones.Funciones import FuncionesGlobales
from funciones.login_Page import Login_Page
from selenium.webdriver.common.action_chains import ActionChains
import time

t=3

class base_test(unittest.TestCase):

    def setUp(self):
        d = FuncionesGlobales()
        d.init(self)

    def test1(self):
        driver = self.driver
        d = FuncionesGlobales(driver)
        d.Navegar("https://demoqa.com/buttons")
        d.Doble_Click("xpath", "//button[contains(@id,'doubleClickBtn')]", t)
        d.Existe("xpath", "//p[contains(@id,'doubleClickMessage')]", t)

    def tearDown(self):
        driver = self.driver
        driver.quit()
        
if __name__ == "__main__":
    unittest.main()