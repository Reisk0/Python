
# Paso 1: recibir palabra o frase
texto = input("Escribe una palabra o frase: ")

# Paso 2: limpiar el texto
texto = texto.lower()    # a minúsculas
texto = texto.replace(" ", "")  # quitar espacios

# Paso 3: invertir
invertido = texto[::-1]

# Paso 4: comparar
if texto == invertido:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")