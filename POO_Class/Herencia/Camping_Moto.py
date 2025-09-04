
class Equipo_Camping: 
    def __init__(self, nombre, motocicleta, mochila):
        self.nombre = nombre
        self.motocicleta = motocicleta
        self.mochila = []

class Campista(Equipo_Camping): 
    def __init__(self, nombre, motocicleta, mochila):
        super().__init__(nombre, motocicleta, mochila)

campista_Motociclista = Campista("Daren", "Ducati")
    
def mostra_mochila(self):
    print(f"{self.nombre} lleva en su equipaje {self.mochila}")

mostra_mochila()