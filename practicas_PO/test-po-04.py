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
from funciones.login_Page import Login_Page
import time

t=3

class base_test(unittest.TestCase):

    def setUp(self):
        d = Funciones_Globales
        d.Init(self)

    def test1(self):
        driver = self.driver
        d = Funciones_Globales(driver)
        d.Navegar("https://testpages.herokuapp.com/styled/file-upload-test.html")
        
        # Obtener la ruta del directorio del script actual
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Construir la ruta relativa al archivo de imagen
        image_path = os.path.join(current_dir, "..", "images", "ice-cream-8195933_640.png")
        
        # Convertir a ruta absoluta
        absolute_image_path = os.path.abspath(image_path)
        
        # Verificar si el archivo existe
        if not os.path.exists(absolute_image_path):
            raise FileNotFoundError(f"La imagen no se encuentra en la ruta: {absolute_image_path}")
        
        d.Upload_ID("fileinput", absolute_image_path, t)
        

    def tearDown(self):
        driver = self.driver
        driver.quit()
        
if __name__ == "__main__":
    unittest.main()