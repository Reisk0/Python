"""
🔹 Reto: Analizador de caracteres

Escribe un programa que:
	1.	Pida al usuario que escriba una frase.
	2.	Cuente cuántos son:
	•	Vocales
	•	Consonantes
	•	Números (ejemplo: 123)
	•	Caracteres especiales (ejemplo: ! , . ? @)
"""

while True:
    entrada = input("Ingresa una frase o escribe 'salir' para terminar: ").lower()

    if entrada == "salir": 
        print("Programa finalizado, muchas gracias.")
        break

    vocales = {"a":0,"e":0,"i":0,"o":0,"u":0}
    consonantes = 0
    numeros = 0
    caracteres = 0

    for posicion in entrada: 
        if posicion in vocales:       # si es vocal
            vocales[posicion] += 1
        elif posicion.isalpha():      # si es consonante
            consonantes += 1
        elif posicion.isdigit():      # si es número
            numeros += 1
        elif not posicion.isspace():  # si no es letra, ni número, ni espacio
            caracteres += 1
            """
                Explicacio de isspace() ⭐️
            •	Si posicion.isspace() → significa que es un espacio, y no lo contamos.
			•	Si no es espacio (not posicion.isspace()), automáticamente es un carácter especial (porque ya sabemos que no es ni vocal, ni consonante, ni número).
            """

    print(f"\nFrase: {entrada}")
    print(f"Vocales: {vocales}")
    print(f"Total de consonantes: {consonantes}")
    print(f"Números: {numeros}")
    print(f"Caracteres especiales: {caracteres}\n")