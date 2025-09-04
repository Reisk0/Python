"""
🧩 Reto: Invertir una cadena

Requisitos:
	1.	Pide al usuario que ingrese una palabra o frase.
	2.	Devuelve esa palabra/frase invertida.
	3.	(Opcional) Haz que ignores espacios en blanco al invertir.
"""

# Pedimos al usuario que escriba una frase
entrada = input("Ingresa una frase,  la invertiremos: ")

# Usamos slicing [::-1] para invertir la cadena:
# - El primer ":" significa "desde el inicio hasta el final"
# - El "-1" indica que vamos recorriendo la cadena hacia atrás

sin_espacios = entrada.replace(" ", "")

invertida = sin_espacios[::-1]

# Mostramos en pantalla la frase invertida
print(invertida)