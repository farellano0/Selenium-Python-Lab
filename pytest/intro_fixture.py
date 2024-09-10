import os
import sys

current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..', 'funciones'))
sys.path.insert(0, parent_dir)

import pytest
from Funciones import FuncionesGlobales
from login_Page import Login_Page

global driver
global funciones
funciones = FuncionesGlobales()
funciones.init()
driver = funciones.driver
login = Login_Page(driver)
t= 1

def setup_function(function):
    print("\nEsto va al inicio de cada test \n")
    
def teardown_function(function):
    print("\nEsto es al final de cada test \n")
    
def test_uno():
    print("Test uno")
    
def test_dos():
    print("Test dos")
    
def test_tres():
    print("Test tres")
    
def test_cuatro():
    print("Test cuatro")