"""
🧩 Reto: Números primos
Escribe un programa en Python que:
	1.	Pida al usuario un número entero positivo n.
	2.	Genere todos los números primos desde 1 hasta n.
	3.	Muestre la lista de los números primos encontrados.
"""
try:
    # Pedimos al usuario un número y tratamos de convertirlo a entero.
    # Si el usuario escribe algo que no sea un número entero, se lanzará ValueError.
    n = int(input("Ingresa un número entero, veremos los números primos: "))
except ValueError:
    # Este bloque se ejecuta si ocurrió un ValueError en la conversión a int.
    # Es decir, si el usuario no ingresó un entero válido.
    print("Valor inválido, trata de nuevo.")
else:
    # Este bloque 'else' del try/except se ejecuta sólo si NO hubo excepción.
    # Aquí continuamos con la lógica cuando la entrada es un entero válido.
    primos = []             # Inicializamos una lista vacía donde guardaremos los primos.

    # Si n < 2, no hay números primos en el rango [2..n], por eso comprobamos n >= 2.
    if n >= 2:
        # Recorremos todos los números desde 2 hasta n inclusive.
        # range(2, n + 1) genera 2, 3, ..., n
        for num in range(2, n + 1):
            es_primo = True  # Variable bandera: asumimos que 'num' es primo hasta demostrar lo contrario.

            # Probamos posibles divisores 'd' desde 2 hasta la raíz cuadrada de 'num'.
            # int(num**0.5) calcula la parte entera de la raíz cuadrada.
            # +1 es necesario porque range no incluye el límite superior,
            # y queremos comprobar divisores exactamente hasta floor(sqrt(num)).
            for d in range(2, int(num**0.5) + 1):
                # Si 'num' es divisible por 'd' (resto 0), entonces no es primo.
                if num % d == 0:
                    es_primo = False  # Marcamos que no es primo.
                    break             # Ya encontramos un divisor, no hace falta seguir buscando.

            # Si después de probar todos los divisores la bandera sigue True, es primo.
            if es_primo:
                primos.append(num)  # Añadimos el número primo a la lista.

    # Mostramos la lista con todos los números primos encontrados (puede ser vacía si n < 2).
    print("Números primos:", primos)