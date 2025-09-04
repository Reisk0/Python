"""
Crea un programa que funcione como un mini menú con estas opciones:
	1.	Saludar al usuario (pide su nombre y muestra un saludo personalizado).
	2.	Mostrar la cantidad de veces que se saludó.
	3.	Salir del programa
"""

# Inicializamos el contador de saludos
contador = 0

# Creamos una lista vacía para guardar los nombres de las personas saludadas
Lista_Saludos = []

# Definimos una función que recibe una lista y un nombre, y agrega ese nombre a la lista
def Funcion_Saludar(saludo, nombre):
    # Agregamos el nombre a la lista de saludos
    saludo.append(nombre)
    """
    •	saludo: es la lista donde queremos guardar los nombres.
	•	nombre: es el nombre del usuario que se va a agregar a esa lista.
    """

# Iniciamos un bucle infinito para mostrar el menú continuamente
while True:
    # Mostramos el menú y pedimos al usuario que elija una opción
    opcion = input("""Elige una opcion del menu:
+++++++++++++
1.- Saludar +
2.- Contar  +
3.- Salir   +
+++++++++++++
Selecciona una opcion: """)

    try:
        # Intentamos convertir la opción ingresada a número entero
        opcion_num = int(opcion)

        # Usamos match-case para elegir la acción dependiendo del número ingresado
        match opcion_num:
            case 1:
                # Si elige 1, pedimos el nombre del usuario
                nombre_usuario = input("Ingresa tu nombre para continuar: ")
                # Mostramos un saludo personalizado
                print(f"que tal {nombre_usuario}, que tengas un excelente dia")
                # Aumentamos el contador de saludos
                contador += 1
                # Llamamos a la función para agregar el nombre a la lista
                Funcion_Saludar(Lista_Saludos, nombre_usuario)

            case 2:
                # Si elige 2, mostramos cuántas veces se ha saludado
                print(f"Numero de saludos {contador}")

            case 3:
                # Si elige 3, mostramos un mensaje de salida
                print(f"Fin del programa, que tengas buen dia.")
                # Mostramos la lista completa de personas que fueron saludadas
                print(f"lista de personas que saludaron {Lista_Saludos}")
                # Salimos del bucle y terminamos el programa
                break

            case _:
                # Si ingresa una opción que no está en el menú, lo avisamos
                print(f"Opcion fuera del menu.")
                # Usamos continue para volver al principio del bucle
                continue

    except ValueError:
        # Si el usuario escribe algo que no es un número, mostramos este mensaje
        print("Por favor, ingresa un número válido.")
        # Y volvemos a pedir la opción al usuario
        continue