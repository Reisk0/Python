
# Creamos un diccionario vacío para almacenar las palabras y la cantidad de vocales en cada una.
diccionario = {}

# Iniciamos un bucle que se repetirá 3 veces para pedir 3 palabras al usuario.
for ciclo in range(3):  
    # Solicitamos al usuario que ingrese una palabra. El método .lower() convierte todo a minúsculas para evitar errores con mayúsculas.
    palabra = input("Ingresa palabra: ").lower()

    # Creamos un contador para contar las vocales en la palabra. Lo inicializamos en 0.
    contador_vocales = 0

    # Iniciamos un bucle que recorre cada letra en la palabra ingresada.
    for letra in palabra:
        # Verificamos si la letra está en la cadena "aeiou" (es decir, si es una vocal).
        if letra in "aeiou":
            # Si la letra es una vocal, sumamos 1 al contador.
            contador_vocales += 1

    # Al final del bucle, guardamos la palabra como clave y el número de vocales como valor en el diccionario.
    diccionario[palabra] = contador_vocales

# Al terminar de procesar las 3 palabras, mostramos el diccionario con el conteo de vocales por palabra.
print(f"Vocales por palabra: {diccionario}")