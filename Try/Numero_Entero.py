# Temas avanzados de Python I
# Ejercicio: Entrada validada y registro de errores

# Abrimos o creamos un archivo llamado "log.txt" para registrar errores.
# El modo 'a' (append) agrega texto sin borrar el contenido anterior.
with open("log.txt", mode="a", encoding="utf-8") as log:

    while True:  # Ciclo infinito hasta que se ingrese un número válido
        entrada = input("Por favor, ingresa un número entero: ")

        try:
            numero = int(entrada)  # Intentamos convertir la entrada a entero
            print(f"✅ ¡Gracias! Has ingresado el número: {numero}")
            break  # Salimos del bucle si la conversión fue exitosa

        except ValueError:
            print("❌ Eso no es un número entero. Intenta de nuevo.")
            log.write(f"❗ Entrada inválida: {entrada}\n")  # Guardamos el error en el archivo log