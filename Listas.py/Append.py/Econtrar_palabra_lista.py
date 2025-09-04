
"""
🎯 Requisitos:
	1.	Usar la lista que ya tienes con tareas (la que contiene los ID y las descripciones).
	2.	Solicitar al usuario una palabra clave.
	3.	Mostrar solo las tareas cuya descripción contenga esa palabra (sin importar mayúsculas/minúsculas).
	4.	Repetir hasta que el usuario escriba "salir".
"""
# Lista de tareas representadas como diccionarios con ID y descripción
lista_de_tareas = [
    {"ID": 1, "Tarea": "Cortar espinas de Rosas"}, 
    {"ID": 2, "Tarea": "Enfriar el vino"}, 
    {"ID": 3, "Tarea": "Arreglar Cabello"}, 
    {"ID": 4, "Tarea": "Buscar vesturario"}, 
    {"ID": 5, "Tarea": "Preparar algo rico de comer"}, 
    {"ID": 6, "Tarea": "Fumar un cigarro colombiano"} 
]

# Iniciamos un bucle infinito para permitir múltiples búsquedas
while True: 
    try: 
        # Lista que almacenará los resultados encontrados en cada búsqueda
        Tareas_encontradas = []

        # Solicitamos al usuario una palabra para buscar en las tareas
        entrada = input("Ingresa una palabra para identificar una tarea o escribe 'salir' para terminar: ") 
        palabra = entrada.lower()  # Convertimos todo a minúsculas para facilitar la comparación

        # Si el usuario escribe "salir", termina el programa
        if palabra == "salir": 
            print("Terminando búsqueda, gracias.")
            break  # Se rompe el ciclo infinito

        # Definimos una función que buscará coincidencias
        def buscar_por_palabra(palabra):
            # Iteramos sobre cada tarea
            for ciclo in lista_de_tareas:
                # Si la palabra ingresada está en la descripción de la tarea (ignorando mayúsculas)
                if palabra in ciclo["Tarea"].lower():
                    # Añadimos esa tarea a la lista de encontradas
                    Tareas_encontradas.append(f"Id de tarea: {ciclo['ID']}. Tarea: {ciclo['Tarea']}")      

        # Ejecutamos la función con la palabra dada por el usuario
        buscar_por_palabra(palabra)

        # Mostramos los resultados encontrados
        print(f"La tarea(s) con la palabra ingresada es/son: {Tareas_encontradas}")
        
    except ValueError:
        # Este bloque solo se ejecutaría si ocurre un error al convertir datos (no hay conversión aquí por ahora)
        print("Dato ingresado inválido.")