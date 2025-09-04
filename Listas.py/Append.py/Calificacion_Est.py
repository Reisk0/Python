
"""
	1.	Permita agregar estudiantes con su nombre y calificación.
	2.	Muestre la lista completa de estudiantes.
	3.	Muestre solo los estudiantes aprobados (calificación mayor o igual a 6).
	4.	Opcional: calcular el promedio general de la clase.
"""

alumnos = [ {"Nombre": "Andre", "Calificación": 8.5}, 
            {"Nombre": "Asmud", "Calificación": 9.5},
            {"Nombre": "Cain", "Calificación": 9.0}, 
            {"Nombre": "Jason", "Calificación": 7.5}, 
            {"Nombre": "Alexandra", "Calificación": 5.5},]

alumnos_aprovados = []


while True: 
    try: 
        estudiante = input("Ingresa el nombre de un estudiante: ")
        calificacion = input("Ingresa su califiacion: ")

        estudiante_cast = str(estudiante)
        calificacion_cast = float(calificacion)
        

        def agregar_alumno(lista, nombre, calificacion):
            nuevo_estudiante = {"Nombre": nombre, "Calificación": calificacion}
            lista.append(nuevo_estudiante)
        
        agregar_alumno(alumnos, estudiante_cast, calificacion_cast)

        print(f"lista de estudiantes {alumnos}")
    except ValueError: 
        print("Dato invalido, trata de nuevo.")