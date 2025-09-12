"""
Objetivo:
Escribir un programa en Python que pida al usuario una palabra o frase y:
	1.	Cuente cuántas vocales contiene.
	2.	Cuente cuántas consonantes contiene.
	3.	Muestre ambos resultados en pantalla.
"""
while True:
    try:
        entrada = str(input("Ingresa una frase: ")).lower()  # Convertimos todo a minúsculas
        vocales = 0
        consonantes = 0

        lista_vocales = ["a", "e", "i", "o", "u"]

        for letra in entrada:
            if letra in lista_vocales:     # Si la letra está en la lista de vocales
                vocales += 1
            elif letra.isalpha():          # Si es una letra (evita contar espacios, números, etc.)
                consonantes += 1
            # Si no es vocal ni letra (ej: espacio, coma, número), lo ignoramos

        # Mostrar resultados
        print(f"\nFrase: {entrada}")
        print(f"Número de vocales: {vocales}")
        print(f"Número de consonantes: {consonantes}")

    except ValueError:
        print("Tipo de dato inválido.")