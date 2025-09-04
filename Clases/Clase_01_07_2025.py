
#Generadores
#   Iterable - una lista de elementos
#   Iterador - como recorro una lista

string = "test" #un objeto que es una lista, recordemos que los strings son listas
objetoiterador = iter(string)#conviertiendo una lista en un iterable
print(objetoiterador)
print(next(objetoiterador)) #t next solo avanzo un paso
print(next(objetoiterador)) #e next solo avanzo un paso
print(next(objetoiterador)) #s next solo avanzo un paso     #test
print(next(objetoiterador)) #t next solo avanzo un paso


#esto puede servir con colecciones de datos muy grandes para no hacer una lista tan gigante y eso nos ahorrara memoria


def __iter__(self): 
    pass

def __next__(self): 
    pass

class FileRead:
    def __init__(self, filename):
        self.file = open(filename, "r")  # Abrimos el archivo en modo lectura

    def __iter__(self):
        return self  # Un iterador debe retornar a sí mismo

    def __next__(self):
        result = self.file.readline()  # Lee una línea del archivo
        if not result:  # Si está vacía (fin del archivo)
            self.file.close()  # Cerramos el archivo
            raise StopIteration  # Terminamos la iteración
        return result.strip()  # Devolvemos la línea sin salto de línea final
    
# Creamos un objeto de tipo FileRead, leyendo el archivo 'datos.txt'
generador = FileRead("datos.txt")

# Usamos next() para obtener manualmente la primera línea
# Esto llama al método __next__() de la clase
print(next(generador))  # Imprime la primera línea del archivo

# Luego usamos un bucle for para seguir leyendo el resto del archivo
# El for continuará desde la segunda línea, porque ya usamos next() antes
for line in generador:
    print("En el el for: " + line)  # Imprime cada línea restante con un prefijo personalizado

