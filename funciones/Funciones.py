from argparse import Action
import os
import sys
import pyperclip
from typing import Literal, Optional
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
import time

class FuncionesGlobales:
    def __init__(self, driver: Optional[webdriver.Chrome] = None, driver_path: str = "C:\\Drivers\\chromedriver.exe"):
        self.service = Service(driver_path)
        self.driver = driver if driver is not None else None
        
    def init(self):
        if self.driver is None:
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
            print(f"No se encontro el elemento {path}")
            raise
    
    def validar_texto(self, selector: Literal["xpath", "id"], path: str, texto: str, tiempo: float):
        element = self._find_element(selector, path)
        element.clear()
        element.send_keys(texto)
        print(f"Texto '{texto}' ingresado en el elemento {path}")
        self.tiempo(tiempo)
    
    def click_valida(self, selector: Literal["xpath", "id"], path: str, tiempo: float):
        element = self._find_element(selector, path)
        try:
            element.click()
            print(f"Click realizado en el elemento {path}")
        except Exception as e:
            print(f"No se dio click: {str(e)}")
            raise
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
    
    def existe(self, selector: Literal["xpath", "id"], path: str, tiempo: float):
        try:
            self._find_element(selector, path)
            print(f"El elemento {path} -> existe")
            self.tiempo(tiempo)
            return True
        except TimeoutException:
            print(f"No se encontró el elemento {path}")
            return False
    
    def doble_click(self, selector: Literal["xpath", "id"], path: str, tiempo: float):
        element = self._find_element(selector, path)
        ActionChains(self.driver).double_click(element).perform()
        print(f"Doble click en -> {path}")
        self.tiempo(tiempo)
        
    def click_derecho(self, selector: Literal["xpath", "id"], path: str, tiempo: float):
        element = self._find_element(selector, path)
        ActionChains(self.driver).context_click(element).perform()
        print(f"Click derecho en -> {path}")
        self.tiempo(tiempo)
        
    def drag_and_drop(self, selector: Literal["xpath", "id"], path_element: str, path_target: str, tiempo: float):
        try:
            element = self._find_element(selector, path_element)
            target = self._find_element(selector, path_target)
            
            ActionChains(self.driver).drag_and_drop(element, target).perform()
            
            print(f"Se arrastró el elemento '{path_element}' al objetivo '{path_target}'")
            self.tiempo(tiempo)
            return True
        except TimeoutException as e:
            print(f"No se pudo encontrar el elemento: {str(e)}")
            return False
        except Exception as e:
            print(f"Error al realizar drag and drop: {str(e)}")
            return False
        
    def drag_and_drop_xy(self, selector: Literal["xpath", "id"], path_element: str, x: int, y: int, tiempo: float):
        try:
            element = self._find_element(selector, path_element)
            
            actions = ActionChains(self.driver)
            actions.drag_and_drop_by_offset(element, x, y).perform()
            
            print(f"Se arrastró el elemento '{path_element}' al punto ({x}, {y})")
            self.tiempo(tiempo)
            return True
        except TimeoutException as e:
            print(f"No se pudo encontrar el elemento: {str(e)}")
            return False
        except WebDriverException as e:
            print(f"Error del WebDriver al realizar drag and drop: {str(e)}")
            return False
        except Exception as e:
            print(f"Error inesperado al realizar drag and drop: {str(e)}")
            return False
        
    def click_xy(self, selector: Literal["xpath", "id"], path_element: str, x: int, y: int, tiempo: float):
        try:
            element = self._find_element(selector, path_element)
            
            actions = ActionChains(self.driver)
            actions.move_to_element_with_offset(element, x, y).click().perform()
            
            print(f"Click al elemento {path_element} coordenada ({x}, {y})")
            self.tiempo(tiempo)
            return True
        except TimeoutException as e:
            print(f"No se pudo encontrar el elemento: {str(e)}")
            return False
        except WebDriverException as e:
            print(f"Error del WebDriver al realizar drag and drop: {str(e)}")
            return False
        except Exception as e:
            print(f"Error inesperado al realizar drag and drop: {str(e)}")
            return False
        
    def key(self, tecla: str):
        """
        Presiona una tecla específica.
        :param tecla: Nombre de la tecla a presionar (e.g., 'tab', 'enter', 'esc')
        """
        teclas = {
            'add': Keys.ADD,
            'alt': Keys.ALT,
            'arrow_down': Keys.ARROW_DOWN,
            'arrow_left': Keys.ARROW_LEFT,
            'arrow_right': Keys.ARROW_RIGHT,
            'arrow_up': Keys.ARROW_UP,
            'backspace': Keys.BACKSPACE,
            'cancel': Keys.CANCEL,
            'clear': Keys.CLEAR,
            'command': Keys.COMMAND,
            'control': Keys.CONTROL,
            'decimal': Keys.DECIMAL,
            'delete': Keys.DELETE,
            'divide': Keys.DIVIDE,
            'down': Keys.DOWN,
            'end': Keys.END,
            'enter': Keys.ENTER,
            'equal': Keys.EQUALS,
            'escape': Keys.ESCAPE,
            'f1': Keys.F1,
            'f2': Keys.F2,
            'f3': Keys.F3,
            'f4': Keys.F4,
            'f5': Keys.F5,
            'f6': Keys.F6,
            'f7': Keys.F7,
            'f8': Keys.F8,
            'f9': Keys.F9,
            'f10': Keys.F10,
            'f11': Keys.F11,
            'f12': Keys.F12,
            'help': Keys.HELP,
            'home': Keys.HOME,
            'insert': Keys.INSERT,
            'left': Keys.LEFT,
            'left_alt': Keys.LEFT_ALT,
            'left_control': Keys.LEFT_CONTROL,
            'left_shift': Keys.LEFT_SHIFT,
            'meta': Keys.META,
            'multiply': Keys.MULTIPLY,
            'null': Keys.NULL,
            'numpad0': Keys.NUMPAD0,
            'numpad1': Keys.NUMPAD1,
            'numpad2': Keys.NUMPAD2,
            'numpad3': Keys.NUMPAD3,
            'numpad4': Keys.NUMPAD4,
            'numpad5': Keys.NUMPAD5,
            'numpad6': Keys.NUMPAD6,
            'numpad7': Keys.NUMPAD7,
            'numpad8': Keys.NUMPAD8,
            'numpad9': Keys.NUMPAD9,
            'page_down': Keys.PAGE_DOWN,
            'page_up': Keys.PAGE_UP,
            'pause': Keys.PAUSE,
            'return': Keys.RETURN,
            'right': Keys.RIGHT,
            'semicolon': Keys.SEMICOLON,
            'separator': Keys.SEPARATOR,
            'shift': Keys.SHIFT,
            'space': Keys.SPACE,
            'subtract': Keys.SUBTRACT,
            'tab': Keys.TAB,
            'up': Keys.UP,
        }
        
        try:
            if tecla.lower() not in teclas:
                raise ValueError(f"Tecla '{tecla}' no soportada")
            
            return teclas[tecla.lower()]
            ActionChains(self.driver).send_keys(teclas[tecla.lower()]).perform()
            print(f"Se presiono la tecla {tecla}")
        except Exception as e:
            print(f"Error al presionar la tecla {tecla}: {str(e)}")
            raise
        
    def salida(self):
        if self.driver:
            self.driver.close()
            
    def quitar(self):
        if self.driver:
            self.driver.quit()
