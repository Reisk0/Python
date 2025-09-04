
# Lista inicial con números repetidos
Lista_Numeros = [1,2,3,4,5,3,4,5,2,10,8,9,7,7,6,6]

# Paso 1: eliminar duplicados
# Convertimos la lista a un conjunto (set) porque los sets no permiten elementos repetidos
numeros_unicos = set(Lista_Numeros)

# Paso 2: convertir el set de nuevo a lista para poder ordenarlo
numeros_unicos = list(numeros_unicos)

# Paso 3: ordenar la lista de menor a mayor
# Paso 3 Plus: Si quisieramos que fuera de mayor a menor ||numeros_unicos.sort(reverse=True)||
numeros_unicos.sort()  # también se podría usar sorted(numeros_unicos)

# Paso 4: imprimir la lista final
print("Lista sin duplicados y ordenada:", numeros_unicos)