Lista_palabras5 = [] # usamos este simbolo para una lista
Lista_palabrasmenos5 = []

for ciclo in range(3):
    palabra = input("Ingresa una palabra: ")
    if len(palabra) > 5: # len(palabra) es una función de Python que devuelve la longitud (número de caracteres) de la cadena (texto) almacenada en palabra.
        print("Palabra mayor a 5 letras, guardada en la lista correspondiente.")
        Lista_palabras5.append(palabra) #✅ append() es un método de las listas en Python. ✅ Se usa para agregar un nuevo elemento al final de la lista.
    else: 
        print("Palabra de hasta 5 letras, guardada en la lista de palabras cortas.")
        Lista_palabrasmenos5.append(palabra)

print(f"Palabras mayores a 5 letras: {Lista_palabras5}")
print(f"Palabras de hasta 5 letras: {Lista_palabrasmenos5}")