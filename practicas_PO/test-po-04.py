import os, sys
parent = os.path.abspath('.')
sys.path.insert(1, parent)

import unittest
from funciones.Funciones import FuncionesGlobales

t= 1

class base_test(unittest.TestCase):

    def setUp(self):
        print("\n--- Iniciando prueba ---")
        self.funciones = FuncionesGlobales()
        self.funciones.init()
        self.driver = self.funciones.driver

    def test1(self):
        print("\nEjecutando test: Inicio de sesion en Sauce Demo")
        self.funciones.navegar("https://testpages.herokuapp.com/styled/file-upload-test.html")
        
        # Obtener la ruta del directorio del script actual
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Construir la ruta relativa al archivo de imagen
        image_path = os.path.join(current_dir, "..", "images", "ice-cream-8195933_640.png")
        
        # Convertir a ruta absoluta
        absolute_image_path = os.path.abspath(image_path)
        
        # Verificar si el archivo existe
        if not os.path.exists(absolute_image_path):
            raise FileNotFoundError(f"La imagen no se encuentra en la ruta: {absolute_image_path}")
        
        self.funciones.upload("id", "fileinput", absolute_image_path, t)
        
        print("Test1 completado")

    def tearDown(self):
        print("\n--- Finalizando prueba ---")
        self.funciones.salida()
        
if __name__ == "__main__":
    unittest.main()