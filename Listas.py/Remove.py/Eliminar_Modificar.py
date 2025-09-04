# Lista de tareas actual
lista = [
    {"ID": 1, "Tarea": "Cortar espinas de Rosas"}, 
    {"ID": 2, "Tarea": "Enfriar el vino"}, 
    {"ID": 3, "Tarea": "Arreglar Cabello"}, 
    {"ID": 4, "Tarea": "Buscar vesturario"}, 
    {"ID": 5, "Tarea": "Preparar algo rico de comer"}, 
    {"ID": 6, "Tarea": "Fumar un cigarro colombiano"} 
]

# Lista donde guardaremos las tareas eliminadas
tareas_Eliminadas = []

# Bucle principal para repetir el proceso
while True: 
    try: 
        # Pedimos al usuario un número de ID para eliminar
        entrada = input("Ingresa el ID de la tarea que deseas eliminar: ")
        dato_ID = int(entrada)  # Convertimos a número

        # Función que busca y elimina la tarea con ese ID
        def Eliminar_tarea(dato_ID):
            for tarea in lista:
                if tarea["ID"] == dato_ID: 
                    tareas_Eliminadas.append(tarea)  # Guardamos la tarea eliminada
                    lista.remove(tarea)              # La quitamos de la lista principal
                    return True  # Indicamos que se realizó correctamente

        # Llamamos la función pasándole el ID ingresado
        llamar_funcion = Eliminar_tarea(dato_ID)

        # Mostramos las listas actualizadas
        print(f"\n✅ Lista de tareas actualizada: {lista}") 
        print(f"🗑️ Tareas eliminadas: {tareas_Eliminadas}\n")

    except ValueError: 
        print("❌ Tarea no encontrada. Ingrésala de nuevo.")