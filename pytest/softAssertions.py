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

@pytest.mark.run
def test_validarif():
    print("primer test")
    assert True

@pytest.mark.run
def test_dos():
    a=10
    b=10
    assert a==b, "No son iguales"
    
@pytest.mark.run
def test_tres():
    a=5
    b=10
    assert a==b, "No son iguales"
    
@pytest.mark.run
def test_cuatro():
    a=15
    b=10
    assert a>b, "A no es mayor que B"
    
@pytest.mark.run
def test_cinco():
    nombre = "Rodrigo"
    b=10
    assert nombre == "RodrigO", "El nombre no es RodrigO"