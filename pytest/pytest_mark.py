import os
import sys
import pytest

# Ruta para importar módulos desde la carpeta 'funciones'
current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..', 'funciones'))
sys.path.insert(0, parent_dir)

from Funciones import FuncionesGlobales
from login_Page import Login_Page


# Tiempo de espera para verificaciones en la UI
WAIT_TIME = 1


@pytest.mark.uno
def test_uno():
    print("Test uno")

@pytest.mark.dos    
def test_dos():
    print("Test dos")

@pytest.mark.tres
def test_tres():
    print("Test tres")
    
@pytest.mark.cuatro
def test_cuatro():
    print("Test cuatro")