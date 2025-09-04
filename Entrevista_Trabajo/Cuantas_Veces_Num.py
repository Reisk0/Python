# Lista de números donde queremos ver cuáles se repiten
numeros = [2, 3, 5, 3, 7, 2, 2, 9, 5, 7]

# Creamos un diccionario vacío donde vamos a guardar el conteo de cada número
contador_numeros = {}

# Recorremos cada número en la lista
for num in numeros:
    # Preguntamos si el número ya está como clave en el diccionario
    if num in contador_numeros:
        # Si ya existe, aumentamos su valor en 1 (porque aparece otra vez)
        # Aquí usamos [num] para acceder al valor asociado a esa clave
        contador_numeros[num] += 1
    else:
        # Si no existe en el diccionario, significa que es la primera vez que aparece
        # Lo agregamos como clave y le asignamos el valor 1
        contador_numeros[num] = 1

# Ahora el diccionario tiene todos los números de la lista como claves
# y cuántas veces aparece cada uno como valor
# Ejemplo: {2: 3, 3: 2, 5: 2, 7: 2, 9: 1}

# Imprimimos un encabezado para indicar que vamos a mostrar los números repetidos
print("Números repetidos y cuántas veces aparecen:")

# Recorremos el diccionario usando .items() para obtener clave y valor a la vez
for num, cantidad in contador_numeros.items():
    # Solo nos interesan los números que aparecen más de una vez
    if cantidad > 1:
        # Imprimimos el número y cuántas veces se repite
        print(f"Número {num} se repite {cantidad} veces")

"""
En resumen:
	•	.keys() → devuelve solo las claves.
	•	.values() → devuelve solo los valores.
	•	.items() → devuelve pares clave-valor.
"""
