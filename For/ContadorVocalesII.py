Vocales = 0  # Inicias un contador para las vocales

entrada = input("Ingresa una frase, la desglozaremos: ").lower()  # Pides una frase y la conviertes a minúsculas

for ciclo in entrada:  # Recorres cada letra de la frase
    if ciclo in("eiou"):  # Si la letra está en el grupo de vocales (excepto 'a')
        Vocales += 1  # Sumas 1 al contador de vocales
    elif ciclo in ("a"):  # Si encuentras una 'a'
        print("¡Encontré una A, así que paro aquí!")  # Imprimes el mensaje
        break  # Detienes el bucle

print(f"La cantidad de vocales en la frase es de: {Vocales}.")  # Imprimes el total de vocales encontradas (sin contar la 'a')