"""
Reto: Contar palabras que empiezan con una letra específica

Requisitos:
	1.	Pide al usuario que ingrese una frase.
	2.	Pide al usuario que ingrese una letra.
	3.	Cuenta cuántas palabras de la frase comienzan con esa letra (ignorando mayúsculas/minúsculas).
	4.	Muestra el conteo y las palabras que coinciden.
"""

entrada = input("Ingresa una frase: ").lower()  # frase en minúsculas
letra = input("Ingresa una letra: ").lower()    # letra en minúsculas

contador = 0
palabras = entrada.split()  # separa la frase en palabras
coincidencias = []          # lista para guardar las palabras que cumplen

for palabra in palabras:
    if palabra.startswith(letra):  # verifica si la palabra comienza con la letra
        contador += 1
        coincidencias.append(palabra)

if contador == 0:  # si ninguna palabra coincidió
    print("Ninguna palabra comienza con esa letra.")
else:
    print(f"Número de palabras que empiezan con '{letra}': {contador}")
    print(f"Palabras: {coincidencias}")