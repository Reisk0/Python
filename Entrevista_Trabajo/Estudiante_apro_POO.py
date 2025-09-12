"""
1️⃣ Clase Estudiante
	•	Crear una clase Estudiante con los atributos:
	1.	nombre → string con el nombre del estudiante
	2.	calificacion → float con la calificación del estudiante
	•	Crear los métodos:
	1.	mostrar_info() → imprime el nombre y la calificación del estudiante
	2.	aprobar() → devuelve True si la calificación es ≥ 6, False si no

⸻

2️⃣ Clase Curso
	•	Crear una clase Curso con el atributo:
	1.	estudiantes → lista que guarda objetos Estudiante
	•	Crear los métodos:
	1.	agregar_estudiante(estudiante) → agrega un estudiante a la lista
	2.	mostrar_aprobados() → recorre la lista y muestra solo los estudiantes que aprobaron

⸻

3️⃣ Interacción con el usuario
	•	Preguntar cuántos estudiantes quiere registrar
	•	Pedir nombre y calificación de cada estudiante
	•	Crear un objeto Estudiante por cada registro y agregarlo al objeto Curso
	•	Al final, mostrar solo los estudiantes aprobados usando el método mostrar_aprobados()

⸻

"""

# --- Clase que representa a un estudiante individual ---
class Estudiante:
    def __init__(self, nombre, calificacion):
        # Guardamos el nombre como string (por seguridad, en caso de que vengan otros tipos)
        self.nombre = str(nombre)
        # Guardamos la calificación como float para poder comparar con >= 6 y mostrar decimales
        self.calificacion = float(calificacion)
        # Atributo booleano que indica si el estudiante ha aprobado.
        # Lo inicializamos en False porque al crear al estudiante asumimos que todavía no fue evaluado.
        self.aprobado = False

    def mostrar_info(self):
        # Construimos una cadena legible para el "estado" usando un operador ternario:
        # Si self.aprobado es True → "✅ Aprobado", si es False → "❌ Reprobado"
        estado = "✅ Aprobado" if self.aprobado else "❌ Reprobado"
        # Imprimimos la información del estudiante en una línea formateada con f-string
        print(f"Estudiante: {self.nombre} | Calificación: {self.calificacion} | Estado: {estado}")
    
    def aprobar(self):
        # Este método decide si marca al estudiante como aprobado o no,
        # basándose en su calificación actual.
        # Si la calificación es mayor o igual a 6, cambia self.aprobado a True.
        if self.calificacion >= 6:
            self.aprobado = True
        # Nota: si quieres que la marca se aplique siempre (incluso para reprobados),
        # podrías añadir un `else: self.aprobado = False` (aunque el atributo ya viene inicializado a False).


# --- Clase que representa un curso, que contiene muchos estudiantes ---
class Curso:
    def __init__(self):
        # Lista donde guardaremos objetos de tipo Estudiante
        self.estudiantes = []
    
    def agregar_estudiante(self, alumno):
        # Agrega el objeto 'alumno' (una instancia de Estudiante) a la lista del curso
        self.estudiantes.append(alumno)

    def mostrar_todos(self):
        # Si la lista está vacía, informamos al usuario
        if not self.estudiantes:
            print("📭 No hay estudiantes aún.")
        # Recorremos todos los estudiantes y llamamos a su método mostrar_info()
        for alumno in self.estudiantes:
            alumno.mostrar_info()

    def mostrar_aprobados(self):
        # Creamos una nueva lista 'aprobados' filtrando self.estudiantes por el atributo aprobado
        aprobados = [a for a in self.estudiantes if a.aprobado]
        # Si la lista filtrada está vacía, informamos que no hay aprobados
        if not aprobados:
            print("❌ No hay estudiantes aprobados.")
        # Para cada alumno aprobado, mostramos su información
        for alumno in aprobados:
            alumno.mostrar_info()


# --- Menú interactivo: aquí usamos las clases anteriores para crear un flujo con el usuario ---
curso_python = Curso()  # Creamos una instancia de Curso donde iremos guardando estudiantes

while True:
    # Mostramos las opciones al usuario
    print("\n📌 Menú")
    print("1. Agregar estudiante")
    print("2. Mostrar todos los estudiantes")
    print("3. Mostrar solo aprobados")
    print("4. Salir")

    try:
        # Pedimos la opción y convertimos a entero. Si el usuario escribe algo no numérico,
        # se lanzará ValueError y caerá al except.
        opcion = int(input("👉 Selecciona una opción: "))

        if opcion == 1:
            # Opción 1: agregar un nuevo estudiante por input
            nombre = input("Nombre del estudiante: ")
            # Convertimos la entrada a float. Si el usuario ingresa algo inválido, saltará ValueError.
            calificacion = float(input("Calificación: "))
            # Creamos la instancia de Estudiante con los datos ingresados
            nuevo = Estudiante(nombre, calificacion)
            # Evaluamos si aprueba; el método cambiará el atributo 'aprobado' si corresponde
            nuevo.aprobar()
            # Agregamos el estudiante al curso
            curso_python.agregar_estudiante(nuevo)
            print("✅ Estudiante agregado.")

        elif opcion == 2:
            # Opción 2: mostramos todos los estudiantes (aprobados y reprobados)
            curso_python.mostrar_todos()

        elif opcion == 3:
            # Opción 3: mostramos solo los estudiantes que están marcados como aprobados
            curso_python.mostrar_aprobados()

        elif opcion == 4:
            # Opción 4: salimos del bucle y finalizamos el programa
            print("👋 Programa finalizado.")
            break

        else:
            # Si el número ingresado no corresponde a ninguna opción
            print("❌ Opción inválida.")

    except ValueError:
        # Capturamos errores de conversión (por ejemplo, si el usuario escribe "hola" cuando pedimos un número)
        print("❌ Ingresa un número válido.")