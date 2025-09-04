# Lista de animales
lista = ["perro", "gato", "ratón", "tigre", "león", "oso", "panda"]

# Clase generadora
class GeneradorAnimales:
    def __init__(self, lista):
        self.lista = lista  # Guardamos la lista
        self.indice = 0     # Inicializamos el índice en 0

    def __iter__(self):
        return self  # Un iterador debe devolver self

    def __next__(self):
        if self.indice < len(self.lista):  # Si aún hay elementos
            valor = self.lista[self.indice]
            self.indice += 1
            return valor
        else:
            raise StopIteration  # Cuando termina

# Creamos la instancia del generador
animales = GeneradorAnimales(lista)

# Consumo con un ciclo for
print("🐾 Animales usando for:")
for animal in animales:
    print(animal)

# También puedes consumirlo con next():
# animales = GeneradorAnimales(lista)
# print(next(animales))
# print(next(animales))