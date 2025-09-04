# Clase base
class Hechicero: 
    def __init__(self, nombre, elemento):
        self.nombre = nombre
        self.elemento = elemento

    def wizard(self): 
        print(f"Mi nombre es {self.nombre}, me especializo en {self.elemento}")

# Clase hija que hereda de Hechicero
class MagoOscuro(Hechicero):  # ← Aquí sí hereda correctamente
    def wizard(self):  # ← Sobrescribimos el método con otro mensaje
        print(f"Yo soy {self.nombre}, el portador de la {self.elemento}...")

# Creamos objetos
mago_luz = Hechicero("Cacian", "Magia Luminus")
mago_oscuridad = MagoOscuro("Lucian", "Magia Tenebris")

# Llamamos a los métodos
mago_luz.wizard()          # Sale: Mi nombre es Cacian, me especializo en Magia Luminus
mago_oscuridad.wizard()    # Sale: Yo soy Lucian, el portador de la Magia Tenebris...




# Clase base
class Criaturas: 
    def __init__(self, nombre, elemento, nivel_de_poder):
        # Constructor que asigna los valores iniciales
        self.nombre = nombre                # Nombre de la criatura
        self.elemento = elemento            # Elemento (fuego, agua, etc.)
        self.nivel_de_poder = nivel_de_poder  # Nivel de poder base

# Clase hija que hereda de Criaturas
class Dragon(Criaturas):
    def presentarse(self): 
        self.nivel_de_poder += 150  # Aumenta el poder base
        print(f"🔥 Mi nombre es {self.nombre}, mi elemento es {self.elemento}, mi nivel de poder es {self.nivel_de_poder}")

# Otra clase hija que también hereda de Criaturas
class Griffo(Criaturas): 
    def presentarse_grifo(self): 
        self.nivel_de_poder += 200  # Aumenta el poder base
        print(f"Mi nombre es {self.nombre}, mi elemento es {self.elemento} y mis puntos de ataque son {self.nivel_de_poder}")

# Otra clase hija que también hereda de Criaturas
class Tempest(Criaturas):
    def presentar_Devian(self):
        self.nivel_de_poder += 500  # Aumenta el poder base
        print(f"Mi nombre es {self.nombre}, mi elemento es {self.elemento} y mis puntos de ataque son {self.nivel_de_poder}")

# Creamos un objeto de la clase Dragon
mi_dragon = Dragon("Altius", "Fuego", 300)

# Creamos un objeto de la clase Griffo
grifindor = Griffo("Gerni", "Viento", 200)

# Creamos un objeto de la clase Tempest
Devian = Tempest("Tempest", "Sangre", 400)

# Llamamos a los métodos de presentación de cada criatura
mi_dragon.presentarse()
grifindor.presentarse_grifo()
Devian.presentar_Devian()