

# Lista vacía donde guardaremos las tareas
Tareas = []

# Variable que contará cuántas tareas se han agregado
Contador_Tarea = 0

# Iniciamos un bucle que se repite hasta que el usuario escriba 'salir'
while True:
    # Pedimos al usuario que ingrese una tarea. Usamos .strip() para quitar espacios al principio y al final
    entrada = input("Ingresa una tarea (escribe 'salir' para terminar): ").strip()

    # Si el usuario escribe 'salir', finalizamos el programa
    if entrada.lower() == "salir":
        print("Programa finalizado.")
        break  # Salimos del bucle

    # Si el usuario presiona solo Enter (deja la entrada vacía), se muestra un mensaje de error
    if entrada == "":
        print("❌ Espacios vacíos no son válidos. Ingresa una tarea válida.")
        continue  # Vuelve al inicio del bucle para pedir otra tarea

    # Definimos una función para agregar una tarea a la lista
    def agregar_tarea(task): 
        global Contador_Tarea  # Indicamos que vamos a usar la variable global Contador_Tarea
        Tareas.append({"Tarea": task})  # Agregamos un diccionario con la tarea a la lista
        Contador_Tarea += 1  # Aumentamos el contador de tareas en 1
        return Tareas  # Devolvemos la lista actualizada

    # Llamamos a la función con la entrada del usuario
    llamar_funcion = agregar_tarea(entrada)

    # Mostramos al usuario que la tarea fue agregada correctamente
    print("✅ Tarea agregada:")
    print(llamar_funcion)  # Mostramos la lista completa de tareas
    print(f"Tareas totales: {Contador_Tarea}")  # Mostramos cuántas tareas se han agregado