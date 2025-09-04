# Definimos la clase Perro
class Perro:
    # Método constructor que se ejecuta al crear el objeto
    def __init__(self, nombre, raza):
        self.nombre = nombre    # Atributo nombre
        self.raza = raza        # Atributo raza

    # Método que hace que el perro ladre
    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")

    # Método para mostrar información del perro
    def info(self):
        print(f"Soy {self.nombre}, y soy un {self.raza}.")

# Este bloque asegura que el código se ejecute solo si corres directamente este archivo
if __name__ == "__main__":
    print("🐾 Iniciando aplicación de mascotas...")

    # Creamos una instancia (objeto) de la clase Perro
    mi_perro = Perro("Sombra", "Labrador")

    # Usamos sus métodos
    mi_perro.ladrar()
    mi_perro.info()