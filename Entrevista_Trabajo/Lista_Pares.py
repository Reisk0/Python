
"""
🧩 Reto: Números pares e impares

Escribe un programa en Python que:
	1.	Pida al usuario un número entero positivo n.
	2.	Genere una lista con los números del 1 al n.
	3.	Separe esos números en pares e impares en listas diferentes.
	4.	Muestre las tres listas en pantalla:
	•	Lista completa
	•	Lista de pares
	•	Lista de impares
"""
try:
    entrada = int(input("Ingresa un número entero: "))  
    # Pide al usuario un valor por teclado y trata de convertirlo a entero.
    # Si la conversión falla (usuario escribe "hola", por ejemplo), se dispara ValueError
except ValueError:
    print("Dato inválido, ingresa un número entero.")  
    # Se ejecuta este bloque si ocurrió ValueError: muestra un mensaje de error
else:
    lista_numeros = []         # Lista vacía para guardar todos los números del 1..entrada
    numeros_pares = []         # Lista vacía para guardar los números pares
    numeros_impares = []       # Lista vacía para guardar los números impares

    # Recorre los números desde 1 hasta 'entrada' **incluyéndolo**
    # range(1, entrada + 1) genera: 1, 2, 3, ..., entrada
    # IMPORTANTE: range(a, b) incluye a y llega hasta b-1, por eso sumamos +1
    for N in range(1, entrada + 1):
        lista_numeros.append(N)        # Agrega el número actual a la lista general

        # Comprueba si N es par: si el resto de dividir por 2 es 0, entonces es par
        if N % 2 == 0:
            numeros_pares.append(N)   # Si es par, lo añade a la lista de pares
        else:
            numeros_impares.append(N) # Si no es par, lo añade a la lista de impares

    # Al terminar el bucle mostramos las listas resultantes
    print("Todos los números:", lista_numeros)
    print("Pares:", numeros_pares)
    print("Impares:", numeros_impares)

    """
    +++IMPORTANTE++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
    +	range(1, entrada + 1) se usa para incluir el número entrada. Si pusieras range(1, entrada) se detendría en entrada - 1.             +
	+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    """