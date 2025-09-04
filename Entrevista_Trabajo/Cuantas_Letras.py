"""
🧩 Reto: Contar caracteres en una cadena

Escribe un programa en Python que:
	1.	Pida al usuario una palabra o frase.
	2.	Cuente cuántas veces aparece cada letra.
	3.	Muestre el resultado en forma de diccionario.
"""

entrada = input("Ingresa un frase, contaremos la letras: ")

lista_letras = {}   # Aquí guardaremos cada letra como clave y sus repeticiones como valor

for letra in entrada:   # Recorremos cada letra de la frase
    if letra in lista_letras:   # Si la letra ya existe en el diccionario AQUI SE CREA EL ENLACE DEL FOR Y EL DICCIONARIO 😀
        lista_letras[letra] += 1   # Aumentamos su contador
    else:   # Si la letra aparece por primera vez
        lista_letras[letra] = 1   # La agregamos al diccionario con valor 1
        
print(f"Lista de caracteres y sus coincidencia: {lista_letras}")


"""
El enlace ocurre en el momento en que escribes lista_letras[letra].
	•	Si no existe, se crea la clave con valor 1.
	•	Si ya existe, se actualiza el valor.
"""