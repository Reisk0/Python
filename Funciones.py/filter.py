
#Objetivo: Filtrar los números pares de una lista.

# Definimos una función que determinará si un número es par
def funcion_filtro(numero): 
    # Usamos el operador módulo (%) para verificar si el número es divisible entre 2
    # Si el resultado es 0, significa que es par y se retorna True
    return numero % 2 == 0

# Creamos una lista de números
numeros = [10, 20, 30, 55, 5, 18]

# Usamos la función filter() para aplicar 'funcion_filtro' a cada elemento de la lista
# filter() devuelve solo los elementos para los que la función retorna True
llamar_funcion = list(filter(funcion_filtro, numeros))  # Convertimos el resultado en una lista

# Imprimimos el resultado
print(f"Los números pares son: {llamar_funcion}")

"""
🧠 ¿Cómo funciona filter()?

La función filter() en Python sirve para filtrar elementos de una colección (como una lista) usando una función que devuelve True o False.
	•	📌 Sintaxis: filter(funcion, iterable)
	•	🔍 Lo que hace: recorre el iterable y solo deja pasar los elementos que hagan que la función retorne True.
	•	🔁 No modifica la lista original, solo devuelve los elementos que cumplen la condición.
"""
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Completa la función que verifica si una palabra tiene 5 letras o más, y luego usa filter() para quedarte solo con esas palabras.
# Definimos una función que devuelve True si la palabra tiene más de 5 letras

def contar_palabras(palabra): 
    return len(palabra) > 5

# Lista de palabras en una oración
frase = ["esta", "es", "una", "palabra", "para", "la", "cual", "se", "utilizara", "un", "len"]

# Aplicamos filter() para quedarnos solo con palabras de más de 5 letras
llamar_funcion_contar = list(filter(contar_palabras, frase))

# Mostramos las palabras filtradas
print(f"Palabras con más de cinco letras: {llamar_funcion_contar}")
#++++++++++++++++++++++++++++++++++++++++++++version mejorada++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Función que verifica si una palabra tiene más de 5 letras
def contar_palabras(palabra): 
    return len(palabra) > 5

# Frase completa en un solo string
frase = "esta es una palabra para la cual se utilizara un len"

# Separamos la frase en palabras usando split()
palabras = frase.split()  # Esto crea una lista de palabras

# Usamos filter() para quedarnos solo con las palabras largas
palabras_largas = list(filter(contar_palabras, palabras))

# Mostramos el resultado
print(f"Palabras con más de cinco letras: {palabras_largas}")

"""
🧠 Explicación clave
	•	frase.split() separa las palabras cada vez que encuentra un espacio y las convierte en una lista:
["esta", "es", "una", "palabra", "para", "la", "cual", "se", "utilizara", "un", "len"]
	•	Luego, filter() aplica la función contar_palabras() a cada una.
"""

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
Objetivo:
	1.	Usa .split() para separar la frase en palabras.
	2.	Usa filter() para quedarte solo con las palabras que comienzan con la letra “p”.
	3.	Guarda el resultado en una lista y muéstrala con un print().
"""

# Definimos una función llamada 'palabras_p' que recibe una palabra como argumento
# y devuelve True si esa palabra comienza con la letra "p", sin importar si es mayúscula o minúscula.
def palabras_p(i): 
    return i.lower().startswith("p")  # Convertimos la palabra a minúsculas y revisamos si empieza con "p"

# Creamos una cadena de texto con varias palabras separadas por espacios
palabras = "puerquito sol palurdo ponce solitario jardin"

# Usamos el método .split() para dividir la cadena en una lista de palabras individuales
# El separador por defecto es el espacio, así que se separan todas las palabras
palabra_conSplit = palabras.split()

# Usamos la función filter() para quedarnos únicamente con las palabras que comienzan con "p"
# filter aplica la función 'palabras_p' a cada elemento de la lista 'palabra_conSplit'
# y mantiene solo aquellos elementos para los que la función devuelve True
llamar_funcionP = list(filter(palabras_p, palabra_conSplit))

# Finalmente, imprimimos el resultado, mostrando solo las palabras que empiezan con "p"
print(f"Estas son las palabras que inician con P: {llamar_funcionP}")