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
import time

t=1

class Login_Page():
    
    def __init__(self, driver):
        self.funciones = FuncionesGlobales(driver)
        
    def Login_Master(self, username, password):
        
        self.funciones.navegar("https://www.saucedemo.com/")
        self.funciones.validar_texto("id", "user-name", username, t)
        self.funciones.validar_texto("id",'password', password, t)
        self.funciones.click_valida("id", 'login-button', t)