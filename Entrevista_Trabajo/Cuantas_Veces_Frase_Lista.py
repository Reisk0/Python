"""
🧩 Reto: Contar palabras únicas

Objetivo:
Escribe un programa en Python que:
	1.	Pida al usuario que ingrese una frase.
	2.	Separe la frase en palabras.
	3.	Cuente cuántas veces aparece cada palabra.
	4.	Muestre todas las palabras y cuántas veces se repiten, ignorando mayúsculas y minúsculas.
"""
# Pedimos al usuario que ingrese una frase y la convertimos a minúsculas
# Esto nos asegura que palabras iguales con diferente capitalización se cuenten como la misma
entrada = input("Ingrese una frase: ").lower()

# Separamos la frase en palabras usando el método split(), 
# lo que nos devuelve una lista de palabras
palabras = entrada.split()#AQUI SE CREA UNA LISTA CON CADA PALABRA DE LA FRASE, TENDRAS QUE RECORRERLA CON UN FOR

# Creamos un diccionario vacío donde almacenaremos la palabra como clave
# y el número de veces que aparece como valor
diccionario_palabra = {}

# Recorremos cada palabra de la lista de palabras
for P in palabras:
    # Si la palabra ya existe como clave en el diccionario,
    # aumentamos su contador en 1
    if P in diccionario_palabra: 
        diccionario_palabra[P] += 1
    # Si la palabra no existe en el diccionario, la agregamos con valor 1
    else:
        diccionario_palabra[P] = 1

# Imprimimos el diccionario resultante, mostrando cuántas veces aparece cada palabra
print(diccionario_palabra)