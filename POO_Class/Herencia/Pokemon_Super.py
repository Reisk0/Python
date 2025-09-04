# Clase base
class Pokemon:  
    def __init__(self, nombre, tipo, CP):
        self.nombre = nombre
        self.tipo = tipo
        self.CP = int(CP)

    def mostrar_info(self):
        print(f"🐾 Nombre: {self.nombre}")
        print(f"⚡ Tipo: {self.tipo}")
        print(f"🔥 CP: {self.CP}")


# Clase hija con un atributo adicional
class Riolu(Pokemon):
    def __init__(self, nombre, tipo, CP, objeto):
        super().__init__(nombre, tipo, CP)  # Heredamos los atributos de Pokemon
        self.objeto = objeto                # Atributo exclusivo de Riolu

    def mostrar_info(self):
        super().mostrar_info()             # Mostramos la info heredada
        print(f"🎁 Objeto equipado: {self.objeto}")  # Y agregamos lo propio


# Otra clase hija sin atributos nuevos
class Zoroark(Pokemon): 
    def __init__(self, nombre, tipo, CP):
        super().__init__(nombre, tipo, CP)


# Clase hija con habilidad especial
class Reshiram(Pokemon): 
    def __init__(self, nombre, tipo, CP, ataque_especial):
        super().__init__(nombre, tipo, CP)
        self.ataque_especial = ataque_especial

    def mostrar_info(self):
        super().mostrar_info()  # Mostramos datos base
        print(f"💥 Ataque especial: {self.ataque_especial}")  # Agregamos el nuevo dato


# Función separadora visual
def separador():
    print("\n" + "=" * 50 + "\n")


# Instancias de cada Pokémon
Team_PM1 = Riolu("Riolu", "Acero", 80, "Collar de Piel")
Team_PM2 = Zoroark("Zoroark", "Fantasma", 80)
Team_PM3 = Reshiram("Reshiram", "Fuego/Dragón", 80, "Blast Fire")

# Mostrar información con separación entre bloques
Team_PM1.mostrar_info()
separador()

Team_PM2.mostrar_info()
separador()

Team_PM3.mostrar_info()
separador()
