# Definimos la clase base llamada Character
class Character:
    # Método constructor, se ejecuta al crear un nuevo objeto
    def __init__(self, nombre, clase):
        self.nombre = nombre      # Guardamos el nombre del personaje
        self.clase = clase        # Guardamos la clase (rol) del personaje

    # Método que imprime una presentación del personaje
    def presentarse(self):
        print(f"Mi nombre es {self.nombre}, mi clase es {self.clase}")

# Definimos una clase llamada Overlord que hereda de Character
class Overlord(Character):  # ← La clase Overlord hereda los atributos y métodos de Character
    # Método propio de Overlord
    def reinar(self):
        print(f"{self.nombre} impone su dominio como un {self.clase}")

# Definimos otra clase llamada Vampire que también hereda de Character
class Vampire(Character):  # ← Herencia desde Character
    # Método propio de Vampire
    def morder(self):
        print(f"{self.nombre} muerde en la oscuridad...")

# Creamos un objeto (instancia) de tipo Overlord
neter = Overlord("Neter", "Señor del Abismo")

# Creamos otro objeto, pero esta vez de tipo Vampire
astius = Vampire("Astius", "Noble - Vampiro")

# Usamos el método heredado presentarse() desde la clase padre
neter.presentarse()  # → Mi nombre es Neter, mi clase es Señor del Abismo

# Usamos el método exclusivo de la clase Overlord
neter.reinar()       # → Neter impone su dominio como un Señor del Abismo

# Usamos el método heredado presentarse() en el vampiro
astius.presentarse() # → Mi nombre es Astius, mi clase es Noble - Vampiro

# Usamos el método exclusivo de la clase Vampire
astius.morder()      # → Astius muerde en la oscuridad...