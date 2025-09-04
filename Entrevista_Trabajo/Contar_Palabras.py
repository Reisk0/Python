entrada = input("Ingresa una oracion: ").lower()
# Solicitamos al usuario una oración y la convertimos a minúsculas para hacer la comparación sin problemas de mayúsculas/minúsculas.

coincidencia = input("Ingresa una palabra para comprobar coincidencia: ").lower()
# Solicitamos al usuario la palabra que quiere buscar y también la pasamos a minúsculas.

contador = 0
# Inicializamos un contador en 0 para llevar la cuenta de cuántas veces aparece la palabra.

for palabra in entrada.split(): 
    # Separamos la oración en palabras usando split() y recorremos cada palabra.
    if palabra == coincidencia: 
        # Si la palabra actual es igual a la que queremos buscar:
        contador += 1
        # Aumentamos el contador en 1.

print(f"La palabra {coincidencia} aparece un total de {contador} veces en la oracion")
# Imprimimos el resultado final mostrando cuántas veces aparece la palabra.
