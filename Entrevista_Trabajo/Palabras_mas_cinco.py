"""
🔹 Reto: Palabras largas

Objetivo: Escribir una función en Python que reciba una lista de palabras y devuelva solo aquellas que tengan más de 5 letras.

🔹 Pasos que espero de ti:
	1.	Crear una función llamada filtrar_palabras_largas(palabras).
	2.	Esa función debe recorrer la lista de palabras.
	3.	Usar una condición (if) para verificar si la palabra tiene más de 5 letras.
	4.	Guardar las palabras que cumplan en una nueva lista.
	5.	Retornar esa lista.
"""

import string
# importamos el módulo `string` porque usaremos `string.punctuation`
# para limpiar signos de puntuación alrededor de las palabras.

def filtrar_palabras_largas(palabras, limite=5):
    """
    Recibe una lista de palabras (strings) y un límite entero.
    Devuelve dos listas: (mas, menos)
    - mas: palabras con longitud > limite
    - menos: palabras con longitud <= limite
    """
    mas = []    # lista que guardará las palabras 'largas'
    menos = []  # lista que guardará las palabras 'cortas'
    for palabra in palabras:
        # Eliminamos espacios al inicio y al final con strip()
        # y además quitamos puntuación exterior (coma, punto, etc.)
        p = palabra.strip().strip(string.punctuation)

        # Si, después de limpiar, la palabra quedó vacía (por ejemplo si el
        # usuario ingresó solo signos), la saltamos para no incluir cadenas vacías.
        if not p:
            continue

        # Aquí podrías normalizar a minúsculas si te interesa:
        # p = p.lower()

        # Si la longitud de la palabra (número de caracteres) es mayor que el límite,
        # la añadimos a la lista 'mas', si no, a 'menos'.
        # Nota: usamos '>' (más de) según el enunciado original (más de 5 letras).
        if len(p) > limite:
            mas.append(p)
        else:
            menos.append(p)

    # Devolvemos ambas listas como una tupla (mas, menos)
    return mas, menos


# Mensaje inicial para el usuario (opcional, sólo para claridad)
print("Escribe palabras separadas por espacios. Escribe 'salir' o deja vacío para terminar.\n")

# Bucle principal: repetimos hasta que el usuario escriba 'salir' o una línea vacía
while True:
    entrada = input("Ingresa palabras: ").strip()
    # .strip() elimina espacios al inicio y final de la cadena ingresada

    # Si el usuario quiere terminar, comprobamos dos condiciones:
    # - escribe "salir" (cualquier combinación de mayúsculas/minúsculas)
    # - o deja la línea vacía (pulsa Enter sin escribir nada)
    if entrada.lower() == "salir" or entrada == "":
        print("Saliendo. ¡Hasta luego!")
        break

    # Convertimos la línea en lista de palabras separadas por espacios.
    # Ej: "hola mundo" -> ["hola", "mundo"]
    lista_palabras = entrada.split()

    # Llamamos a la función que procesa y clasifica las palabras.
    # Devuelve dos listas: palabras con más de 5 letras y las demás.
    mas_de_cinco, menos_de_cinco = filtrar_palabras_largas(lista_palabras, limite=5)

    # Mostramos los resultados de forma legible
    print(f"Palabras con más de cinco letras: {mas_de_cinco}")
    print(f"Palabras con cinco o menos letras: {menos_de_cinco}\n")