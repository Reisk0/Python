# Abre el archivo "hola.txt" en modo lectura ('r'), con codificación UTF-8.
# Se usa "with" para que el archivo se cierre automáticamente al terminar de usarlo.
with open("hola.txt", mode='r', encoding='utf-8') as f:

    # Recorre cada línea del archivo usando enumerate, que también da el número de línea (i)
    for i, linea in enumerate(f):

        # Imprime el número de línea (i + 1 porque enumerate comienza en 0)
        # y el contenido de esa línea. 
        # .strip() elimina espacios y saltos de línea al final.
        print(f"Línea {i + 1}: {linea.strip()}")