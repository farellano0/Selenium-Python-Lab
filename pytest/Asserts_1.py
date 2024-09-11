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

@pytest.mark.skip
def test_validar_if():
    nom1 = "Rodrigo"
    nom2 = "Rodrigo"
    
    assert nom1==nom2, "Los nombre no son iguales"

@pytest.mark.skip    
def test_in():
    dato = "RAM"
    frase = "Dentro de las computadoras hay memoria RAM"
    
    assert dato in frase, "El dato no está dentro de la frase."
    
# @pytest.mark.skip
def test_assert_if():
    a=20
    b=25
    if(a==b):
        assert True, "Los datos son iguales"
    else:
        assert False, "Los datos nos son iguales"