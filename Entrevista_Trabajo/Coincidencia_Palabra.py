"""
🎯 Reto 2: Contador de palabras

Crea un programa que:
	1.	Pida al usuario que ingrese una frase.
	2.	Muestre:
	•	Cuántas palabras hay en total.
	•	Cuántas veces aparece cada palabra.
	3.	Ignore mayúsculas/minúsculas (ejemplo: "Hola" y "hola" cuentan igual).
"""
# Pedimos al usuario que ingrese una frase y la convertimos a minúsculas
# para que "Hola" y "hola" se consideren la misma palabra.
entrada = input("Ingrese una palabra: ").lower()  

# Inicializamos un contador para el total de palabras
total_palabras = 0  

# Creamos un diccionario vacío donde guardaremos las palabras como claves
# y el número de veces que aparece cada palabra como valor
diccionario_palabras = {}  

# Separamos la frase en palabras usando el espacio como separador.
# Esto devuelve una lista de palabras.
lista_palabra = entrada.split()  

# Iteramos sobre cada palabra de la lista
for palabra in lista_palabra:  
    # Cada vez que encontramos una palabra, incrementamos el contador total
    total_palabras += 1  

    # Verificamos si la palabra ya está en el diccionario
    if palabra in diccionario_palabras:  
        # Si existe, aumentamos en 1 su contador
        diccionario_palabras[palabra] += 1  
    else:  
        # Si no existe, la agregamos al diccionario con valor 1
        diccionario_palabras[palabra] = 1  #⚠ El momento en que le “decimos” al programa que meta la palabra en el diccionario es en la línea del else:

# Mostramos la frase original ingresada (en minúsculas)
# Nota: '\a' genera un sonido de alerta, puedes quitarlo si no quieres el beep
print(f"Frase: \a{entrada}")  

# Mostramos el diccionario con la cantidad de veces que aparece cada palabra
print(f"Coincidencias: {diccionario_palabras}.")  

# Mostramos el número total de palabras encontradas en la frase
print(f"Total de palabras: {total_palabras}.")  