"""
🧩 Ejercicio: Palíndromos

Un palíndromo es una palabra o frase que se lee igual al derecho y al revés (ignorando espacios, mayúsculas, acentos y signos de puntuación).

👉 Tu reto será escribir un programa en Python que:
	1.	Pida al usuario una palabra o frase.
	2.	Convierta todo a minúsculas.
	3.	Ignore los caracteres especiales (.,!? etc.).
	4.	Verifique si es un palíndromo.
	5.	Muestre un mensaje indicando si lo es o no.
"""

while True: 
    # Pedimos al usuario que ingrese una frase
    # La función .lower() convierte todo a minúsculas para evitar problemas con mayúsculas
    entrada = input("Ingresa una frase, identificaremos palindromos o escribe salir para terminar: ").lower()

    # Creamos una lista vacía donde guardaremos las palabras que sean palíndromos
    palindromo = []

    # Separamos la frase en palabras usando split() (por defecto separa por espacios)
    palabra_palabra = entrada.split()

    # Condición de salida: si el usuario escribe "salir", finalizamos el programa
    if entrada == "salir": 
        print("Fin del programa, Buen día.")
        break
    
    # Recorremos cada palabra de la lista
    for palabra in palabra_palabra: 
    # Saltamos palabras que contengan caracteres que no sean letras
        if not palabra.isalpha(): 
            continue
        # Verificamos si la palabra es igual a sí misma al revés
        elif palabra == palabra[::-1]:
            # Si es palíndromo, la agregamos a la lista
            palindromo.append(palabra)
    
    # Mostramos la frase original
    print(f"Frase: \n{entrada}.")
    # Mostramos las palabras palíndromas encontradas
    print(f"Palindromo(s): \n{palindromo}.")