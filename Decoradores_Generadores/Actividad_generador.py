
# Lista de animales
lista = ["perro", "gato", "ratón", "tigre", "león", "oso", "panda"]

class GeneradorAnimales:
    # Constructor, lo llevan todas las clases
    def __init__(self, lista):
        # asignamos parametros del contructor
        # como atributos de clase
        self.indice=0
        self.lista=lista
    
    # se llama la funcion cuando lo convertimos
    # a iterable para darle contexto
    def __iter__(self):
        return self
    
    # next regresa el resultado y prepara la siguiente iteracion
    def __next__(self):
        # si el indice d ela lista es menor al tamaño de
        # la lista, traes un resultado, sino levantas la exepcion
        if self.indice< len(self.lista):
            # creas una variable a partir del elemnto de la lista en el indice alamacenado
            valor = self.lista[self.indice]
            # incrementas 1 el indice
            self.indice+=1
            # regresas el valor
            return valor
        else:
            #aqui levantas al exepcion
            raise StopIteration

class GeneradorAnimalesYield:
    def __init__(self, datos):
        self.datos = datos  # Lista de elementos a iterar

    def __iter__(self):
        # Usamos yield para generar los valores uno a uno
        for animal in self.datos:
            yield animal

generador = GeneradorAnimales(lista)
print("Desde next", next(generador))
print("Desde next", next(generador))

generador_con_for = GeneradorAnimales(lista)
for item in generador_con_for:
    print("Desde for:",item)
