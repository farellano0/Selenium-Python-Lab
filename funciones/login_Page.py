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

t=2

class Login_Page():
    
    def __init__(self, driver):
        self.driver = driver
        
    def Login_Master(self, username, password):
        driver = self.driver
        d = Funciones_Globales(driver)
        d.Navegar("https://www.saucedemo.com/")
        d.Validar_Texto("//input[contains(@id,'user-name')]", username, t)
        d.Validar_Texto("//input[@id='password']", password, t)
        d.Click_Xpath_Valida("//input[@id='login-button']", t)