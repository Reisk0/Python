# Bucle infinito para permitir al usuario ingresar varias frases
while True:
    try:
        # Pedimos al usuario que ingrese una frase y la convertimos a minúsculas
        entrada = input("Ingresa una frase: ").lower()

        # Diccionario para contar las vocales
        vocales_contador = {"a":0, "e":0, "i":0, "o":0, "u":0}

        # Diccionario para contar las consonantes
        consonantes_contador = {}

        # Recorremos cada letra de la frase
        for letra in entrada:
            # Ignoramos cualquier caracter que no sea letra
            if letra.isalpha():
                # Si la letra es una vocal, incrementamos su contador
                if letra in vocales_contador:
                    vocales_contador[letra] += 1
                # Si la letra no es vocal, entonces es consonante
                else:
                    if letra not in consonantes_contador:
                        consonantes_contador[letra] = 1  # inicializamos contador
                    else:
                        consonantes_contador[letra] += 1  # incrementamos contador

        # Imprimimos la frase original
        print(f"\nFrase: {entrada}")

        # Contamos el total de vocales y consonantes sumando los valores de los diccionarios
        total_vocales = sum(vocales_contador.values())
        total_consonantes = sum(consonantes_contador.values())

        print(f"Numero total de vocales: {total_vocales}")
        print(f"Detalle de vocales: {vocales_contador}")

        print(f"Numero total de consonantes: {total_consonantes}")
        print(f"Detalle de consonantes: {consonantes_contador}")

    except ValueError:
        print("Tipo de dato invalido, intenta nuevamente.")