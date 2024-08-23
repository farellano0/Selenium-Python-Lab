import os
import sys
from typing import Literal
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time

class FuncionesGlobales:
    def __init__(self, driver_path: str = "C:\\Drivers\\chromedriver.exe"):
        self.service = Service(driver_path)
        self.driver = None
        
    def init(self):
        chrome_options = Options()
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--ignore-ssl-errors')
        self.driver = webdriver.Chrome(service=self.service, options=chrome_options)
        self.driver.implicitly_wait(15)
        
    @staticmethod
    def tiempo(segundos: float):
        time.sleep(segundos)
        
    def navegar(self, url: str):
        self.driver.get(url)
        self.driver.maximize_window()
        print(f"Pagina abierta: {url}")
    
    def _find_element(self, selector: Literal["xpath", "id"], path: str) -> webdriver.remote.webelement.WebElement:
        by = By.XPATH if selector == "xpath" else By.ID
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, path)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            return element
        except TimeoutException:
            print(f"No se encontró el elemento {path}")
            raise
    
    def validar_texto(self, selector: Literal["xpath", "id"], path: str, texto: str, tiempo: float):
        element = self._find_element(selector, path)
        element.clear()
        element.send_keys(texto)
        print(f"Texto '{texto}' ingresado en el elemento {path}")
        self.tiempo(tiempo)
    
    def click_valida(self, selector: Literal["xpath", "id"], path: str, tiempo: float):
        element = self._find_element(selector, path)
        element.click()
        print(f"Click realizado en el elemento {path}")
        self.tiempo(tiempo)
    
    def select_type(self, selector: Literal["xpath", "id"], path: str, tipo: Literal["text", "index", "value"], dato: str | int, tiempo: float):
        element = self._find_element(selector, path)
        select = Select(element)
        if tipo == "text":
            select.select_by_visible_text(dato)
        elif tipo == "index":
            select.select_by_index(dato)
        elif tipo == "value":
            select.select_by_value(dato)
        self.tiempo(tiempo)
    
    def upload(self, selector: Literal["xpath", "id"], path: str, ruta: str, tiempo: float):
        element = self._find_element(selector, path)
        element.send_keys(ruta)
        print(f"Se carga la imagen {ruta}.")
        self.tiempo(tiempo)
    
    def check(self, selector: Literal["xpath", "id"], path: str, tiempo: float):
        element = self._find_element(selector, path)
        element.click()
        print(f"Click en el elemento {path}.")
        self.tiempo(tiempo)
    
    def check_xpath_multiples(self, tiempo: float, *args: str):
        for path in args:
            self.check("xpath", path, tiempo)
    
    def existe(self, selector: Literal["xpath", "id"], path: str, tiempo: float) -> Literal["Existe", "No Existe"]:
        try:
            self._find_element(selector, path)
            print(f"El elemento {path} -> existe")
            self.tiempo(tiempo)
            return "Existe"
        except TimeoutException:
            print(f"No se encontró el elemento {path}")
            return "No Existe"
    
    def doble_click(self, selector: Literal["xpath", "id"], path: str, tiempo: float):
        element = self._find_element(selector, path)
        ActionChains(self.driver).double_click(element).perform()
        print(f"Doble click en → {path}")
        self.tiempo(tiempo)
    
    def salida(self):
        if self.driver:
            self.driver.quit()