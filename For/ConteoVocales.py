# Creamos un diccionario para contar cada vocal
conteo_vocales = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

# Solicitamos al usuario una cadena de texto
cadena = input("Ingresa una cadena de texto: ")

# Recorremos cada letra de la cadena
for letra in cadena.lower():
    # Si la letra es una vocal, la contamos
    if letra in conteo_vocales:
        conteo_vocales[letra] += 1

# Mostramos los resultados
print("\nCantidad de veces que aparece cada vocal:")
for vocal, cantidad in conteo_vocales.items():
    print(f"{vocal}: {cantidad}")