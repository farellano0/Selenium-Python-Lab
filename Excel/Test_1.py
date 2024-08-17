import email
from Funciones_Ex import *
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

t = 1

class base_test(unittest.TestCase):
    def setUp(self):
        d = Funciones_Globales
        d.Init(self)

    def test1(self):
        driver = self.driver
        fg = Funciones_Globales(driver)
        fe = FunExcel(driver)
        fg.Navegar("https://demoqa.com/text-box")
        ruta = os.path.abspath("Excel/Datos_ok.xlsx")
        filas=fe.getRowCount(ruta,"Hoja1")
        
        for r in range(2, filas+1):
            nombre=fe.readData(ruta, "Hoja1", r, 1)
            email=fe.readData(ruta, "Hoja1", r, 2)
            dir1=fe.readData(ruta, "Hoja1", r, 3)
            dir2=fe.readData(ruta, "Hoja1", r, 4)
            
            fg.Validar_Texto("id", "userName", nombre, t)
            fg.Validar_Texto("id", "userEmail", email, t)
            fg.Validar_Texto("id", "currentAddress", dir1, t)
            fg.Validar_Texto("id", "permanentAddress", dir2, t)
            fg.Click_Valida("id", "submit", t)
            
            e=fg.Existe("id", "name", t)
            if(e=="Existe"):
                print("El elemento se inserto correctamente")
                fe.writeData(ruta, "Hoja1", r, 5, "Insertado")
            else:
                print("No se inserto")
                fe.writeData(ruta, "Hoja1", r, 5, "Error")
                
        

    def tearDown(self):
        driver = self.driver
        driver.quit()
        
if __name__ == "__main__":
    unittest.main()