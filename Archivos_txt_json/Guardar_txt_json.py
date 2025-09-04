# Paso 1: Pedimos al usuario que ingrese un mensaje
mensaje = input("📝 Ingresa un mensaje: ")

# Función para guardar en formato TXT
def guardar_como_txt(mensaje):
    with open("mensaje.txt", "w", encoding="utf-8") as archivo:
        archivo.write(mensaje)
    print("✅ Mensaje guardado en 'mensaje.txt'")

# Función para guardar en formato JSON
import json

def guardar_como_json(mensaje):
    contenido = {"mensaje": mensaje}
    with open("mensaje.json", "w", encoding="utf-8") as archivo:
        json.dump(contenido, archivo, indent=4, ensure_ascii=False)
    print("✅ Mensaje guardado en 'mensaje.json'")   

# Paso 2: Creamos un bucle para seleccionar el formato
while True:
    try:
        # Mostramos opciones de formato
        formato = input("\n📂 ¿En qué formato deseas guardar el mensaje?\n1.- txt\n2.- json\nSelecciona: ")

        if formato == "1":
            print("💾 Guardando como .txt...")
            guardar_como_txt(mensaje)  # ✅ Aquí se pasa el mensaje
            break

        elif formato == "2":
            print("💾 Guardando como .json...")
            guardar_como_json(mensaje)  # ✅ Aquí también se pasa el mensaje
            break

        else:
            print("❌ Opción inválida. Elige 1 o 2.")

    except ValueError:
        print("⚠️ Error. Intenta de nuevo.")

#EXPLICACION DE LAS FUNCIONES PARA GUARDAR EN FORMATO

#DEF TXT
#1.    def guardar_como_txt(mensaje):
# -(mensaje) → Esto indica que la función recibe un parámetro llamado mensaje. Este será el texto que el usuario haya escrito.

#2.    with open("mensaje.txt", "w", encoding="utf-8") as archivo:
#   with open(...) as archivo: → Esta línea abre o crea un archivo llamado mensaje.txt.
#	"mensaje.txt" → Es el nombre del archivo de texto que queremos crear o sobrescribir.
#   "w" → Significa write (escribir). Si el archivo ya existe, lo sobrescribe. Si no existe, lo crea.
#   encoding="utf-8" → Esto garantiza que se pueden guardar acentos, ñ y caracteres especiales sin errores.
#   archivo → Es un nombre temporal (una “etiqueta”) para el archivo dentro del bloque with.

#3.    archivo.write(mensaje)
#   	•	archivo.write(...) → Escribe el contenido de mensaje dentro del archivo.
#	    •	En este caso, se guarda exactamente lo que escribió el usuario cuando se le pidió el mensaje.

#ARCHIVO (aclaracion para no confundirlo)
"""
📌 archivo es solo un nombre de variable temporal que representa el archivo abierto.
Específicamente:
	•	Cuando haces open("mensaje.txt", "w", encoding="utf-8"), estás abriendo un archivo para escribir en él.
"""

# DEF JSON

#1.contenido = {"mensaje": mensaje}
#👉 Aquí se está creando un diccionario de Python con una sola clave llamada "mensaje".

#2 with open("mensaje.json", "w", encoding="utf-8") as archivo:
#👉 Esto abre un archivo llamado mensaje.json en modo escritura ("w"), y lo prepara para guardar contenido.
#	•	"mensaje.json": nombre del archivo a crear o sobrescribir.
#	•	"w": modo escritura (si ya existe el archivo, lo sobrescribe).
#	•	encoding="utf-8": asegura que se escriban caracteres especiales correctamente (tildes, ñ, etc.).
#	•	archivo: variable temporal que representa el archivo abierto (como ya viste antes).

#3  json.dump(contenido, archivo, indent=4, ensure_ascii=False)
#  👉 Esta línea es la que guarda el diccionario como un JSON real dentro del archivo.
#•	json.dump(...): función de la biblioteca json que convierte un diccionario en texto JSON y lo guarda directamente en un archivo.
#	•	contenido: el diccionario que queremos guardar.
#	•	archivo: el archivo donde lo escribiremos.
#	•	indent=4: organiza el JSON con indentación de 4 espacios, para que sea más legible.
#	•	ensure_ascii=False: permite guardar caracteres especiales (como tildes o emojis) correctamente, sin convertirlos a código Unicode.