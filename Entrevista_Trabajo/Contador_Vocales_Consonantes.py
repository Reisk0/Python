"""
🔹 Reto: Contador de vocales y consonantes

👉 Escribe un programa en Python que:
	1.	Pida al usuario que ingrese una frase.
	2.	Cuente cuántas vocales y cuántas consonantes hay en la frase.
	3.	Ignore los espacios y los caracteres especiales (solo debe contar letras).
	4.	Muestre el total de vocales y consonantes por separado.
"""

# Iniciamos un ciclo infinito para que el programa se repita hasta que el usuario escriba "salir"
while True: 
    # Pedimos al usuario que ingrese una frase
    # .lower() convierte toda la frase a minúsculas para simplificar la comparación
    entrada = input("Ingresa una frase o escribe 'salir' para terminar: ").lower()
    
    # Si el usuario escribe "salir", se muestra un mensaje y se rompe el ciclo con break
    if entrada == "salir": 
        print("Ejercicio terminado, gracias.")
        break

    # Creamos un diccionario para almacenar las vocales y la cantidad de veces que aparecen
    # Cada vocal es una "clave" y su valor empieza en 0
    lista_vocales = {"a":0,"e":0,"i":0,"o":0,"u":0}

    # Inicializamos un contador para las consonantes
    numero_consonantes = 0

    # Recorremos la frase letra por letra
    for letra in entrada: 
        # Si la letra es una vocal (está en las claves del diccionario)
        # se incrementa el valor de esa vocal en el diccionario
        if letra in lista_vocales: 
            lista_vocales[letra] += 1
        # Si no es vocal, verificamos si es una letra del alfabeto (isalpha() devuelve True si es letra)
        elif letra.isalpha():  
            numero_consonantes += 1   # sumamos 1 al contador de consonantes

    # Calculamos el total de vocales sumando todos los valores del diccionario
    total_vocales = sum(lista_vocales.values())

    # Mostramos los resultados
    print(f"\nFrase: {entrada}")  # La frase ingresada
    print(f"Vocales por tipo: {lista_vocales}")  # Cuántas veces aparece cada vocal
    print(f"Total de Vocales: {total_vocales}")  # El total de todas las vocales
    print(f"Número de Consonantes: {numero_consonantes}\n")  # El número de consonantes