"""
La herencia permite que una clase nueva (llamada clase hija) tome atributos y métodos de otra clase existente (llamada clase padre).
"""

# Definimos una clase base llamada Animal
class Animal:
    # Método constructor que se ejecuta al crear una instancia de Animal
    def __init__(self, nombre):
        self.nombre = nombre  # Atributo de instancia: el nombre del animal
                                # Guardamos el nombre en el objeto

    # Método común que podría ser compartido o sobrescrito
    def hablar(self): 
        print("Hace un sonido genérico")  # Mensaje genérico


# Definimos una clase hija llamada Perro que hereda de Animal
class Perro(Animal):
    # Sobrescribimos el método hablar solo para Perro
    def hablar(self):
        print(f"{self.nombre} dice: ¡Guau!")  # Mensaje específico para perros


# Definimos otra clase hija llamada Gato que también hereda de Animal
class Gato(Animal):
    # Sobrescribimos el método hablar solo para Gato
    def hablar(self):
        print(f"{self.nombre} dice: ¡Miau!")  # Mensaje específico para gatos


# Creamos un objeto (instancia) de la clase Perro
mi_perro = Perro("Firulais")  # Se llama al constructor de Animal con nombre = "Firulais"

# Creamos un objeto (instancia) de la clase Gato
mi_gato = Gato("Michi")  # Se llama al constructor de Animal con nombre = "Michi"

# Llamamos al método hablar de cada objeto
mi_perro.hablar()  # Imprime: Firulais dice: ¡Guau!
mi_gato.hablar()   # Imprime: Michi dice: ¡Miau!


"""
Piensa en una clase como una receta de pastel.
	•	__init__ es el momento de preparar la mezcla inicial (ingredientes específicos).
	•	self es el pastel que estás haciendo, el objeto real.

Cada vez que haces un pastel (creas un objeto), usas la receta (class), y el constructor (__init__) 
te ayuda a poner ingredientes (atributos) en ese pastel (objeto).
"""