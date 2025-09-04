import json

def guardar_txt(entrada):
    with open("Mensaje_texto2.txt", "w", encoding="utf-8") as archivo:
        archivo.write(entrada)
    print("✅ Mensaje guardado en formato TXT.")

def guardar_json(entrada):
    # Creamos un diccionario en Python que tendrá una sola clave llamada "mensaje"
    # El valor de esa clave será lo que el usuario escribió (la variable 'entrada')
    diccionario = {"mensaje": entrada}
    with open("Mensaje_json2.json", "w", encoding="utf-8") as archivo:
        json.dump(diccionario, archivo, indent=4, ensure_ascii=False)
    print("✅ Mensaje guardado en formato JSON.")

while True:
    entrada = input("📝 Ingresa un mensaje: ")
    try:
        mensaje = input("\n📂 ¿En qué formato deseas guardar el mensaje?\n1.- txt\n2.- json\n3.- salir\nOpción seleccionada: ")

        if mensaje == "1":
            guardar_txt(entrada)
            continue
        elif mensaje == "2":
            guardar_json(entrada)
            continue
        elif mensaje == "3":
            print("📁 Mensajes guardados. Fin del programa.")
            break
        else:
            print("❌ Opción inválida, selecciona 1, 2 o 3.")
    except ValueError:
        print("⚠️ Error: entrada inválida.")