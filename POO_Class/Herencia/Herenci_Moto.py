# Clase base
class Moto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encender = False
        self.velocidad = 0

    def encender_moto(self):
        self.encender = True
        print(f"La motocicleta está encendida. Marca: {self.marca}, Modelo: {self.modelo}.")

    def velocidad_maxima(self):
        self.velocidad += 230
        print(f"Velocidad máxima de {self.marca} {self.modelo} es de {self.velocidad} km/h.")

# Clase hija que hereda de Moto
class Harley(Moto):
    def velocidad_maxima(self):
        self.velocidad += 180
        print(f"Velocidad máxima de {self.marca} {self.modelo} es de {self.velocidad} km/h.")

class Indian_Scout(Moto):
    def velocidad_maxima(self):
        self.velocidad += 185
        print(f"Velocidad máxima de {self.marca} {self.modelo} es de {self.velocidad} km/h.")

# Crear objetos de ambas clases
ducati = Moto("Ducati", "Monster")
harley_davidson = Harley("Harley-Davidson", "Iron 808")
Indian =  Indian_Scout("Indian", "Rebellion")



# Usar los métodos
ducati.encender_moto()
ducati.velocidad_maxima()

harley_davidson.encender_moto()
harley_davidson.velocidad_maxima()


Indian.encender_moto()
Indian.velocidad_maxima()
