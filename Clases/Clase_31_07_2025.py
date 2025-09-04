#Pruebas en Python
#Categorias de pruebas: Manuales y Automaticas
#Caso de uso: acciones o situaciones que que el usuario puede hacer en la aplicacion
#Caso de prueba: son las situaciones que vamos a simular

#Recordemos que el software son cajas negras
#Algo entra algo sale
#Siempre que se ingrese lo mismo sale lo mismo

#Unittest 🐦‍🔥 
#Pytest
#Robot
#DocTest
#Nose2
#Testify

#Franework - marco de trabajo, es la caja de herramientas entera
#Es un conjunto de herramientas que nos permite realizar una tarea de manera mas efectiva

#Libreria - es solo una herramienta (no debemos confundirla con un franework)

import unittest # es parte de la SL por que no necesitamos gestor de librerias

class MisCasosdePrueba(unittest.TestCase): # la clase es un portafolio donde podremos tener diversas pruebas 
    # Como consejo es preferencial ser descriptivo con los nombres incluso implementar un patron que sea test y el nombre del metodo a probar
    #Imaginemos que esta funcion es una checklist que debemos de palomear cada pruena y solo podremos decir que estuvo bien si nunca hubo un falso
    def test_suma(self): 
        #resultado imaginemoslo como el resultado de alguna funcion que tuvieramos en algun lado
        #respuesta es_mayor_de_edad (18)
        resultado = 2+3
        #Esta prueba va a estar bien si el resulta es igual al resultado esperado
        #[scope].assertEqual (lo que nos van a traer y lo que esperamos que nos traigan)
        self.assertEqual(resultado, 5)
        self.assertEqual(15>18, False)

    def test_random(self): 
        self.assertEqual(45 == "Amigo", True)

if __name__ == "__main__":
    unittest.main() # si no me especicas ningun metodo 

#Metodo tearDownModule() y setUoModule() estos son metodos que se ejecutan antes de las pruebas

