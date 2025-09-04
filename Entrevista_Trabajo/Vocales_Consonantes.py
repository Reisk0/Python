"""
🧩 Reto: Contar vocales y consonantes en una frase

Escribe un programa en Python que:
	1.	Pida al usuario una oración.
	2.	Cuente cuántas vocales (a, e, i, o, u) hay en total.
	3.	Cuente cuántas consonantes hay.
	4.	Muestre el resultado.
"""

# Pedimos al usuario que ingrese una oración
entrada = input("Ingresa una oración: ").lower()  # Convertimos a minúsculas para facilitar la comparación

# Definimos las vocales
lista_vocales = ["a", "e", "i", "o", "u"]

# Inicializamos los contadores
vocales = 0
consonantes = 0

# Recorremos cada letra de la oración
for letra in entrada:
    if letra.isalpha():  # Verificamos que sea una letra
        if letra in lista_vocales:  # Si la letra es una vocal
            vocales += 1
        else:  # Si es letra pero no es vocal, entonces es consonante
            consonantes += 1

# Mostramos el resultado
print(f"Número de vocales: {vocales}")
print(f"Número de consonantes: {consonantes}")