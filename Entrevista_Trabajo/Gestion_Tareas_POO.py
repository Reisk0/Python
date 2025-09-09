"""
🚀 Reto: Gestión de Tareas (POO)

Crea una clase llamada Tarea con los siguientes atributos:
	•	titulo (str)
	•	descripcion (str)
	•	completada (bool, empieza en False)

Y los siguientes métodos:
	1.	marcar_completada() → cambia el estado de la tarea a completada.
	2.	mostrar_info() → imprime el título, descripción y estado (“✅ completada” o “❌ pendiente”).

Luego, crea una clase llamada ListaTareas que permita:
	•	Guardar varias tareas en una lista interna.
	•	Agregar nuevas tareas.
	•	Mostrar todas las tareas con su información.
	•	Mostrar solo las tareas pendientes.
"""
# --- Clase que representa una tarea individual ---
class Tarea: 
    def __init__(self, titulo, descripcion):
        self.titulo = titulo             # Guardar el título de la tarea
        self.descripcion = descripcion   # Guardar la descripción de la tarea
        self.completada = False          # Estado inicial: la tarea no está completada

    def marcar_completada(self):
        self.completada = True           # Cambiar el estado a completada
        print(f"La tarea '{self.titulo}' fue completada exitosamente.")  # Mensaje de confirmación

    def mostrar_info(self):
        # Operador ternario: si self.completada es True, mostrar ✅ Completada, sino ❌ Pendiente
        estado = "✅ Completada" if self.completada else "❌ Pendiente"
        # Imprimir toda la información de la tarea en una línea
        print(f"Tarea: {self.titulo} | Descripción: {self.descripcion} | Estado: {estado}")


# --- Clase que representa una lista de tareas ---
class ListaDeTareas: 
    def __init__(self):
        self.tareas = []  # Lista vacía donde se almacenarán los objetos Tarea

    # Método para agregar una tarea a la lista
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)  # Añadir objeto Tarea a la lista

    # Método para mostrar todas las tareas
    def mostrar_todas(self):
        if not self.tareas:                # Si la lista está vacía
            print("📭 No hay tareas aún.") # Mensaje de aviso
        for tarea in self.tareas:          # Si hay tareas
            tarea.mostrar_info()           # Mostrar la información de cada tarea

    # Método para mostrar solo las tareas pendientes
    def mostrar_pendientes(self):
        # Crear una lista solo con tareas no completadas
        pendientes = [t for t in self.tareas if not t.completada]
        if not pendientes:                 # Si no hay tareas pendientes
            print("🎉 No hay tareas pendientes.")  # Mensaje de aviso
        for tarea in pendientes:           # Si hay tareas pendientes
            tarea.mostrar_info()           # Mostrar info de cada pendiente

    # Método para marcar una tarea como completada usando su índice
    def marcar_completada(self, indice):
        try:
            self.tareas[indice].marcar_completada()  # Llamar al método de la tarea correspondiente
        except IndexError:                            # Si el índice no existe
            print("❌ No existe una tarea con ese número.")  # Mensaje de error


# --- Crear la lista principal de tareas ---
lista = ListaDeTareas()

# --- Bucle principal del menú interactivo ---
while True: 
    try:
        # Mostrar el menú
        print("\n📌 Menú de Tareas")
        print("1.- Agregar una tarea")
        print("2.- Mostrar todas las tareas")
        print("3.- Mostrar tareas pendientes")
        print("4.- Marcar tarea como completada")
        print("5.- Salir")

        # Solicitar al usuario que seleccione una opción
        comando = int(input("👉 Selecciona una opción: "))

        if comando == 1:
            # Agregar nueva tarea
            titulo = input("Título de la tarea: ")      # Pedir título
            descripcion = input("Descripción: ")        # Pedir descripción
            nueva = Tarea(titulo, descripcion)          # Crear objeto Tarea
            lista.agregar_tarea(nueva)                  # Agregar tarea a la lista
            print("✅ Tarea agregada.")

        elif comando == 2:
            # Mostrar todas las tareas
            lista.mostrar_todas()

        elif comando == 3:
            # Mostrar solo tareas pendientes
            lista.mostrar_pendientes()

        elif comando == 4:
            # Marcar una tarea como completada
            lista.mostrar_todas()  # Primero mostrar todas las tareas con sus índices
            indice = int(input("👉 Ingresa el número de la tarea a completar (empezando desde 0): "))
            lista.marcar_completada(indice)  # Marcar la tarea seleccionada como completada

        elif comando == 5:
            # Salir del programa
            print("👋 Programa finalizado, gracias.")
            break

        else:
            # Si el usuario ingresa un número fuera de rango
            print("❌ Opción inválida.")

    except ValueError: 
        # Si el usuario no ingresa un número
        print("❌ Ingresa un número válido.")