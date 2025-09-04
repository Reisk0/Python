"""
🧩 Reto: Números divisibles

Objetivo:
Escribe un programa en Python que:
	1.	Pida al usuario un número entero n.
	2.	Cree una lista con los números del 1 al n.
	3.	Separe los números en tres listas diferentes:
	•	divisibles_por_2 → números divisibles por 2
	•	divisibles_por_3 → números divisibles por 3
	•	divisibles_por_5 → números divisibles por 5
	4.	Muestre cada lista con un mensaje claro indicando qué números contiene.
"""


# Listas vacías para guardar los números y los divisibles
lista_n = []
divisible_dos = []
divisible_tres = []
divisible_cinco = []

try:
    # Pedimos al usuario un número entero (la cantidad de números que queremos generar)
    n = int(input("Ingresa una cantidad: "))

    # Generamos los números desde 1 hasta n (incluyendo n, por eso usamos n+1)
    for num in range(1, n+1):  
        lista_n.append(num)  # Guardamos cada número en la lista general

        # Si el número es divisible entre 2, lo agregamos a su lista
        if num % 2 == 0: 
            divisible_dos.append(num)

        # Si es divisible entre 3, lo agregamos a la lista correspondiente
        if num % 3 == 0: 
            divisible_tres.append(num)

        # Si es divisible entre 5, lo agregamos a su lista
        if num % 5 == 0: 
            divisible_cinco.append(num)   

    # Mostramos los resultados al usuario
    print(f"Lista de numeros: {lista_n}")
    print(f"Divisibles entre 2 {divisible_dos}")
    print(f"Divisibles entre 3 {divisible_tres}")
    print(f"Divisibles entre 5 {divisible_cinco}")

# Si el usuario no ingresa un número entero, mostramos un error controlado
except ValueError:
    print("Cantidad invalida: ")
