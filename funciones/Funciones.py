import os, sys
parent = os.path.abspath('.')
sys.path.insert(1, parent)

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

class Funciones_Globales():
    
    def __init__(self, driver):
        self.driver = driver
        
    def Init(self):
        self.service = Service("C:\\Drivers\\chromedriver.exe")
        self.driver = webdriver.Chrome(service = self.service)
        self.driver.implicitly_wait(15)
        
    def Tiempo(self, tiempo):
        t = time.sleep(tiempo)
        return t
    
    def Navegar(self, url):
        self.driver.get(url)
        self.driver.maximize_window()
        print(f"Página abierta {url}")
    
    def Validar_Texto(self, selector, path, texto, tiempo):
        if(selector=="xpath"):
            try:
                val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, path)))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", val)
                val.clear()
                val.send_keys(texto)
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print(f"No se encontró el elemento {path}")
        elif(selector=="id"):
            try:
                val = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, path)))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", val)
                val.clear()
                val.send_keys(texto)
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print(f"No se encontró el elemento {path}")
    
            
    def Click_Valida(self, selector, path, tiempo):
        if(selector=="xpath"):
            try:
                btn = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, path)))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
                btn.click()
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print(f"No se encontró el elemento {path}")
        elif(selector=="id"):
            try:
                btn = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, path)))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", btn)
                btn.click()
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print(f"No se encontró el elemento {path}")
            
            
    def Select_Type(self, selector, path, tipo, dato, tiempo):
        if(selector=="xpath"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, path)))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", val)
                val = Select(val)
                if (tipo=="text"):
                    val.select_by_visible_text(dato)
                elif (tipo=="index"):
                    val.select_by_index(dato)
                elif (tipo=="value"):
                    val.select_by_value(dato)
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print(f"No se encontró el elemento {path}")
        elif(selector=="id"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, path)))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", val)
                val = Select(val)
                if (tipo=="text"):
                    val.select_by_visible_text(dato)
                elif (tipo=="index"):
                    val.select_by_index(dato)
                elif (tipo=="value"):
                    val.select_by_value(dato)
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print(f"No se encontró el elemento {path}")
            
    def Upload(self, selector, path, ruta, tiempo):
        if(selector=="xpath"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, path)))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", val)
                val.send_keys(ruta)
                print(f"Se carga la imagen {ruta}.")
                
                t = time.sleep(tiempo)
                return t
            
            except TimeoutException as ex:
                print(ex.msg)
                print(f"No se encontró el elemento {path}")
        elif(selector=="id"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, path)))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", val)
                val.send_keys(ruta)
                print(f"Se carga la imagen {ruta}.")
                
                t = time.sleep(tiempo)
                return t
            
            except TimeoutException as ex:
                print(ex.msg)
                print(f"No se encontró el elemento {path}")
            
    # Función Radio y Check
    def Check(self, selector, path, tiempo):
        if(selector=="xpath"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, path)))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", val)
                val.click()
                print(f"click en el elemento {path}.")
                
                t = time.sleep(tiempo)
                return t
            
            except TimeoutException as ex:
                print(ex.msg)
                print(f"No se encontró el elemento {path}")
        elif(selector=="id"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, path)))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", val)
                val.click()
                print(f"click en el elemento {path}.")
                
                t = time.sleep(tiempo)
                return t
            
            except TimeoutException as ex:
                print(ex.msg)
                print(f"No se encontró el elemento {path}")
            
            
    def Check_Xpath_Multiples(self, path, tiempo, *args):
        try:
            for n in args:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, n)))
                self.driver.execute_script("arguments[0].scrollIntoView(true);", val)
                val.click()
                print(f"click en el elemento {path}.")
                
                t = time.sleep(tiempo)
                return t
            
        except TimeoutException as ex:
            for n in args:
                print(ex.msg)
                print(f"No se encontró el elemento {n}")
            
    def Salida(self):
        print("Se termina la prueba Exitosamente")