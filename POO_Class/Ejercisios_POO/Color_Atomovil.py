"""
Definir una nueva clase “vehículo” con los atributos que requiera, pero que incluya el atributo “color”
Agregue un método llamado “cambia_color” que reciba un nuevo color como entrada y que modifique
el atributo de color del objeto.
Agregar otro método que imprima el color del vehículo.
Una vez definida la clase cree una instancia de esa clase, y haga que cambie el color del vehículo, al
final imprima el color nuevo del vehículo.
"""
class Vehiculo: 
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = int(año)
        self.color = color

    def cambia_color(self, nuevo_color):
        self.color = nuevo_color

    def mostrar_color(self): 
        print(f"Color del vehículo: {self.color}")

class MiAuto(Vehiculo):
    def __init__(self, marca, modelo, año, color):
        super().__init__(marca, modelo, año, color)

# Creamos el objeto
mi_automovil = MiAuto("Honda", "Civic", 2019, "Rojo")

# Pedimos nuevo color
nuevo_color = input("Ingresa el color para tu auto: ")
mi_automovil.cambia_color(nuevo_color)
mi_automovil.mostrar_color()