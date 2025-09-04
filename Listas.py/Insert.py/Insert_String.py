
"""
	2.	Pide al usuario:
	•	Una nueva tarea (string).
	•	Una posición numérica donde quiera colocarla.
	3.	Usa insert(posición, nueva_tarea) para agregarla en esa posición.
	4.	Imprime la lista actualizada.
"""
tareas = ["Leer", "Estudiar", "Ejercitarse"]

while True: 
    try: 
        entrada = input("Ingresa una tarea (o escribe 'salir' para terminar): ")

        # Salir si el usuario escribe "salir"
        if entrada.lower() == "salir": 
            print("Fin del programa, tareas terminadas.")
            break

        posicion = input("Ingresa la posición donde deseas insertar la tarea: ")

        # Convertimos la entrada a string y la posición a número entero
        entrad_str = str(entrada)
        posicion_int = int(posicion) 

        # Función que inserta la nueva tarea en la posición indicada
        def insertar_tarea(lista):
            return lista.insert(posicion_int, entrad_str)
        
        insertar_tarea(tareas) # “😎Ejecuta la función insertar_tarea, y usa la lista tareas como entrada”.

        # Mostramos la lista actualizada
        print(f"\n📝 Lista de tareas actualizada: {tareas}")

    except ValueError: 
        print("❌ Dato inválido. Asegúrate de ingresar un número para la posición.")