"""
🎯 Reto propuesto:

Problema:
Crea un programa en Python que pida al usuario una lista de calificaciones (separadas por comas) y muestre:
	1.	El promedio de las calificaciones.
	2.	La calificación más alta y la más baja.
	3.	Cuántas calificaciones son aprobatorias (mayores o iguales a 6).
"""

try:
    # Pedir lista de calificaciones separadas por comas
    entrada = input("Ingresa una lista de calificaciones separadas por comas: ")

    # Separar por comas y convertir cada valor a entero
    lista_calificaciones = [int(num) for num in entrada.split(",")] #+++++++++++++++
    """
    Esta liena equivale a hacer esto
    lista_calificaciones = []
        for num in entrada.split(","):
            lista_calificaciones.append(int(num))
    """

    # Calcular valores
    mayor = max(lista_calificaciones)
    menor = min(lista_calificaciones)
    promedio = sum(lista_calificaciones) / len(lista_calificaciones)

    # Mostrar resultados
    print(f"Mayor calificación: {mayor}")
    print(f"Menor calificación: {menor}")
    print(f"Promedio de calificaciones: {promedio:.2f}")

except ValueError:
    print("Dato inválido, ingresa solo números separados por comas.")