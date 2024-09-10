import os
import sys

current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..', 'funciones'))
sys.path.insert(0, parent_dir)

import pytest
from Funciones import FuncionesGlobales

t= 1

@pytest.fixture(scope='module')
def setup_login_uno():
    print("\nEmpezando el login del sistema uno")
    yield
    print("\nSaliendo del sistema prueba ok")

@pytest.fixture(scope="module")
def setup_login_dos():
    print("\nEmpezando las pruebas del sistema dos")
    yield
    print("\nFin de las pruebas del sistema dos")
    

def test_uno(setup_login_uno):
    print("\n--- EMPEZANDO LAS PRUEBAS DEL TEST UNO ---\n")
    
    
def test_dos(setup_login_dos):
    print("\n--- EMPEZANDO LAS PRUEBAS DEL TEST DOS ---\n")


@pytest.mark.usefixtures("setup_login_dos")    
def test_dos():
    print("\n--- EMPEZANDO LAS PRUEBAS DEL TEST TRES LOGIN DOS ---\n")