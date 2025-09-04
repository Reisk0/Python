"""
🧩 Reto: Contar cuántas veces aparece cada vocal
	1.	Pide al usuario que ingrese una oración.
	2.	Recorre cada letra de la oración (ignora mayúsculas y caracteres que no sean letras).
	3.	Cuenta cuántas veces aparece cada vocal (a, e, i, o, u).
	4.	Al final, muestra el número de apariciones de cada vocal.
"""

entrada = input("Ingresa una frase: ")

entrada_minus = entrada.lower()

vocales = ["a","e","i","o","u"]

list_vocales = {"a":0, 
                "e":0,
                "i":0, 
                "o":0, 
                "u":0}

for letra in entrada_minus: 
    
    if letra in vocales: 
        list_vocales[letra] += 1

print(list_vocales)

"""
 👉 Cada vez que el bucle encuentra una vocal (por ejemplo "o"), esta línea le suma 1 al contador de "o" en el diccionario.

Ejemplo paso a paso con "Hola":
	•	Diccionario inicial: {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
	•	Iteración 1: letra "h" → no hace nada.
	•	Iteración 2: letra "o" → list_vocales["o"] += 1 → ahora "o":1.
	•	Iteración 3: letra "l" → no hace nada.
	•	Iteración 4: letra "a" → list_vocales["a"] += 1 → ahora "a":1.
."""