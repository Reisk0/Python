from datetime import datetime
class Personaje: 
    def __init__(self, nombre, edad, ocupacion, caracteristica):
        self.nombre = nombre
        self.edad = int(edad)
        self.ocupacion = ocupacion
        self.caracteristica = caracteristica

    def presentar_personaje(self): 
        print(f"Un gusto, mi nombre es {self.nombre}, \aActualmente tengo {self.edad} años de edad.")
        print(f"Mi ocupación actual es {self.ocupacion}. \aRespecto a mí, {self.caracteristica}")
    
    def conversar(self, mensaje): 
        fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
        linea = f"[{fecha_hora_actual}] {self.nombre} dice: {mensaje}"
        with open("Conversacion.txt", "a", encoding="utf8") as archivo: 
            archivo.write(linea + "\n")

    def mostrar_conversacion(self): 
        with open ("Conversacion.txt", "r", encoding="utf8") as archivo: 
            contenido_conversacion = archivo.read()
            print(contenido_conversacion)


    def editar_conversacion(self):
        try:
            # 1️⃣ Abrimos el archivo en modo lectura para obtener todas las líneas
            with open("Conversacion.txt", "r", encoding="utf8") as archivo:
                lineas = archivo.readlines() # Este método lee todo el archivo completo y devuelve una lista, donde cada elemento es una línea del archivo.

            # 2️⃣ Verificamos si el archivo está vacío
            if not lineas:
                print("⚠ No hay conversaciones para editar.")
                return  # Salimos del método

            # 3️⃣ Mostramos todas las líneas con un índice
            print("\n--- Conversación actual ---")
            for i, linea in enumerate(lineas): # enumerate() es una función de Python que recorre un iterable (en este caso, la lista lineas)
                print(f"[{i}] {linea.strip()}")  # strip() quita el salto de línea al final

            # 4️⃣ Pedimos al usuario que elija la línea a editar
            indice = int(input("\nEscribe el número de línea que deseas editar: "))

            # 5️⃣ Validamos que el índice esté dentro del rango
            if indice < 0 or indice >= len(lineas):
                print("❌ Índice fuera de rango.")
                return

            # 6️⃣ Pedimos el nuevo mensaje
            nuevo_mensaje = input("Escribe el nuevo mensaje: ")

            # 7️⃣ Mantenemos la fecha y hora original (opcional)
            partes = lineas[indice].split("] ", 1)  # Dividimos en fecha y resto
            if len(partes) == 2:
                fecha_hora, _ = partes
                lineas[indice] = f"{fecha_hora}] {self.nombre} dice: {nuevo_mensaje}\n"
            else:
                # Si no encontramos el formato esperado, simplemente reemplazamos la línea
                lineas[indice] = nuevo_mensaje + "\n"

            # 8️⃣ Reescribimos el archivo con las líneas modificadas
            with open("Conversacion.txt", "w", encoding="utf8") as archivo:
                archivo.writelines(lineas)
            print("✅ Mensaje editado correctamente.")

        except FileNotFoundError:
            print("❌ No existe el archivo de conversación.")
        except ValueError:
            print("⚠ Entrada inválida, por favor ingresa un número.") 
            

class Jaden(Personaje): 
    pass

jaden = Jaden("Jaden Evans", 25, "Programador-Diseñador", "Creo tener un rostro sereno y agradable, tomo café sin azúcar")

Porciones_en_taza = 5

while True:
    interaccion = input("\nEvan comenzará a interactuar: \n1.- Conversar \n2.- Observar y escuchar a nuestro acompañante \n3.- Tomar un sorbo de café \n4.- Ver toda la conversacion\n5.- Cambiar lo que dijiste\n6.- Borrar lo que dijiste\n7.- Salir\nElige una opción: ")

    if interaccion == "1":
        mensaje = input("¿Qué es lo que te gustaría decir? ")
        jaden.conversar(mensaje)
        print("Mensaje guardado.")
    elif interaccion == "2":
        print("Observas atentamente a tu acompañante y asientes cuando te pregunta algo.")
    elif interaccion == "3":
        if Porciones_en_taza > 0:
            Porciones_en_taza -= 1
            print(f"Tomas un sorbo de café. Porciones restantes: {Porciones_en_taza}")
            if Porciones_en_taza == 0:
                print("Parece que terminé mi café sin darme cuenta. Pediré otra a la mesera en un momento.")
                print("¿Quieres algo para ti?")
            else:
                print("No quedan más porciones de café.")
    elif interaccion == "4": 
            jaden.mostrar_conversacion()
    elif interaccion == "5": 
            jaden.editar_conversacion()
    elif interaccion == "6": 
            pass
    elif interaccion == "7":
        print("Terminando la interacción. ¡Hasta luego!")
        break
    else:
        print("Esa opción no es válida, por favor selecciona otra.")



        #EXPLICACION COMO USAR DATE TIME 
"""

            def conversar(self, mensaje): 
        fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
        linea = f"[{fecha_hora_actual}] {self.nombre} dice: {mensaje}"
        with open("Conversacion.txt", "a", encoding="utf8") as archivo: 
            archivo.write(linea + "\n")
        from datetime import datetime  # IMPORTANTE: asegúrate de esto al principio del archivo
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def conversar(self, mensaje):                                                                          +
    # datetime.now() -> obtiene la fecha y hora actual como objeto datetime                            +
    # .strftime("%Y-%m-%d %H:%M:%S") -> formatea ese objeto en una cadena legible:
    # "AÑO-MES-DÍA HORA:MINUTO:SEGUNDO"
    fecha_hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Construimos la línea que se escribirá en el archivo.
    # Usamos f-string para insertar la fecha/hora, el nombre del personaje (self.nombre)
    # y el mensaje que nos pasan como argumento.
    # Ejemplo resultante: "[2025-08-11 09:12:34] Jaden Evans dice: Hola"
    linea = f"[{fecha_hora_actual}] {self.nombre} dice: {mensaje}"

    # Abrimos el archivo "Conversacion.txt" en modo "a" (append) para añadir al final sin borrar lo existente.
    # encoding="utf8" asegura que podamos escribir caracteres especiales (tildes, ñ, etc.).
    # El bloque `with` garantiza que el archivo se cierre automáticamente al terminar (incluso si ocurre un error).
    with open("Conversacion.txt", "a", encoding="utf8") as archivo:
        # Escribimos la línea formada en el archivo y añadimos '\n' para que cada mensaje quede en una nueva línea.
        archivo.write(linea + "\n")
"""