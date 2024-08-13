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
from funciones.Funciones import Funciones_Globales
import time

class base_test(unittest.TestCase):

    def setUp(self):
        d = Funciones_Globales
        d.Init(self)

    def test1(self):
        driver = self.driver
        d = Funciones_Globales(driver)
        d.Navegar("https://www.saucedemo.com/")
        d.Validar_Texto("//input[contains(@id,'user-name')]", "Fernando", 3)
        d.Validar_Texto("//input[@id='password']", "secret_sauce", 3)
        d.Click_Xpath_Valida("//input[@id='login-button']", 3)
        

    def tearDown(self):
        driver = self.driver
        driver.quit()
        
if __name__ == "__main__":
    unittest.main()