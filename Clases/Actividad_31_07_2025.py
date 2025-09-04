"""
Genere el script de pruebas unitarias usando la librería de unittest para el siguiente programa,
deberá de probar las funciones de suma, resta y multiplicacion:
def suma(a, b):
return a + b
def resta(a, b):
return a – b
def multiplicacion(a, b):
return a * b
"""

import unittest  # Importamos el módulo para realizar pruebas automatizadas (unitarias)

# Definimos una función que suma dos números
def suma(a, b):
    return a + b

# Definimos una función que resta el segundo número al primero
def resta(a, b):
    return a - b

# Definimos una función que multiplica dos números
def multiplicacion(a, b):
    return a * b

# Creamos una clase que hereda de unittest.TestCase, donde escribiremos nuestras pruebas
class MiPruebaEjercicio(unittest.TestCase):

    # Método para probar si la función 'suma' funciona correctamente
    def test_suma(self): 
        self.assertEqual(suma(2, 5), 7)        # 2 + 5 = 7
        self.assertEqual(suma(0, 0), 0)        # 0 + 0 = 0
        self.assertEqual(suma(-2, 3), 1)       # -2 + 3 = 1
        self.assertEqual(suma(-3, -4), -7)     # -3 + (-4) = -7

    # Método para probar si la función 'resta' funciona correctamente
    def test_resta(self): 
        self.assertEqual(resta(10, 3), 7)      # 10 - 3 = 7
        self.assertEqual(resta(-1, 1), -2)     # -1 - 1 = -2
        self.assertEqual(resta(-2, 3), -5)     # -2 - 3 = -5
        self.assertEqual(resta(-3, -4), 1)     # -3 - (-4) = 1

    # Método para probar si la función 'multiplicacion' funciona correctamente
    def test_multiplicacion(self): 
        self.assertEqual(multiplicacion(2, 5), 10)     # 2 * 5 = 10
        self.assertEqual(multiplicacion(0, 0), 0)      # 0 * 0 = 0
        self.assertEqual(multiplicacion(2, 10), 20)    # 2 * 10 = 20
        self.assertEqual(multiplicacion(-3, -4), 12)   # -3 * -4 = 12 (negativo por negativo da positivo)

# Este bloque permite ejecutar las pruebas solo si el archivo se ejecuta directamente desde la terminal
if __name__ == '__main__':
    unittest.main(verbosity=2)  # Ejecuta las pruebas con más detalle en la salida (verbose)