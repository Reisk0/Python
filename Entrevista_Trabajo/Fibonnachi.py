"""
🧩 Reto: Secuencia de Fibonacci

Escribe un programa en Python que:
	1.	Pida al usuario un número entero n.
	2.	Genere la secuencia de Fibonacci hasta el número n de términos.
	3.	Muestre la secuencia completa en pantalla.
"""

# Pedimos al usuario la cantidad de términos que quiere generar
try:
    n = int(input("Ingresa un número entero positivo: "))
    if n <= 0:
        print("❌ Por favor ingresa un número mayor que 0")
    else:
        # Creamos una lista vacía para almacenar la secuencia
        fibonacci = [0,1]


        # Generamos el resto de la secuencia
        for i in range(2, n): #range 2 hace que la secuencia se comience a contar a partir del tercer caracter
            # Cada término es la suma de los dos anteriores
            siguiente = fibonacci[i-1] + fibonacci[i-2]
            fibonacci.append(siguiente)

        # Mostramos la secuencia completa
        print(f"Secuencia de Fibonacci con {n} términos:")
        print(fibonacci)

except ValueError:
    print("❌ Dato inválido, debes ingresar un número entero")



    """
    Si tienes una lista fibonacci = [0, 1]:
	•	fibonacci[0] → primer elemento → 0
	•	fibonacci[1] → segundo elemento → 1

Cuando i = 2 (tercer elemento que estamos calculando):
	•	fibonacci[i-1] = fibonacci[1] = 1 → el segundo elemento
	•	fibonacci[i-2] = fibonacci[0] = 0 → el primer elemento

Entonces i-1 y i-2 no se refieren a la posición “2 y 1” si contamos desde 1, sino a los índices de la lista empezando desde 0.
    """