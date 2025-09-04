"""
Vas a modificar tu sistema de tareas para permitir al usuario insertar una nueva tarea en una posición específica (ID) de la lista.

🧭 Guía paso a paso:
	1.	Pídele al usuario la tarea nueva (como ya lo haces).
	2.	Luego, pídele en qué posición desea insertarla (por ejemplo, después de la tarea con ID 2).
	3.	Convierte esa posición a índice de lista (recuerda que los índices empiezan en 0).
	4.	Usa insert() para agregar el diccionario de la nueva tarea en esa posición.
	5.	Muestra la lista actualizada.

"""

# Lista de tareas inicial
lista_de_tareas = [
    {"ID": 1, "Tarea": "Cortar espinas de Rosas"},
    {"ID": 2, "Tarea": "Enfriar el vino"},
    {"ID": 3, "Tarea": "Arreglar Cabello"},
    {"ID": 4, "Tarea": "Buscar vestuario"},
    {"ID": 5, "Tarea": "Preparar algo rico de comer"},
    {"ID": 6, "Tarea": "Fumar un cigarro colombiano"}
]

# Bucle infinito para permitir múltiples inserciones
while True:
    try:
        # Pedimos al usuario un ID (posición en la lista)
        posicion = input("🔢 Ingresa una posición (ID) para insertar la nueva tarea (o escribe 'salir' para terminar): ")
        
        if posicion.lower() == "salir":
            print("✅ Programa terminado.")
            break  # Finaliza el bucle si el usuario lo indica

        # Convertimos a número entero
        casteo_id = int(posicion)

        # Pedimos la descripción de la tarea
        entrada = input("✏️ Ingresa la descripción de la nueva tarea: ")
        casteo_entrada = str(entrada)

        # Creamos un nuevo diccionario con la tarea
        nueva_tarea = {"ID": casteo_id, "Tarea": casteo_entrada}

        # Insertamos la tarea en la posición indicada (si es válida)
        if 0 <= casteo_id <= len(lista_de_tareas):  # Validamos rango
            lista_de_tareas.insert(casteo_id, nueva_tarea)
            print("📌 Nueva tarea insertada correctamente.")
        else:
            print("❌ Posición fuera de rango. Intenta con otro número.")
            continue  # Vuelve al inicio del ciclo

        # Mostramos la lista actualizada
        print("\n📝 Lista de tareas actualizada:")
        for tarea in lista_de_tareas:
            print(f"ID: {tarea['ID']} - Tarea: {tarea['Tarea']}")

    except ValueError:
        print("❌ Entrada inválida. Asegúrate de ingresar un número entero para el ID.")