# Paso 1: Declaramos la función usando 'def' y le damos un nombre descriptivo.
# Paso 2: Entre paréntesis indicamos que la función necesita un parámetro: 'lado'.
def calcular_area_cuadrado(lado):
    
    # Paso 3: Dentro de la función, calculamos el área del cuadrado.
    area = lado * lado

    # Paso 4: Usamos 'return' para devolver el resultado al lugar donde se llamó la función.
    return area

# Paso 5: Llamamos a la función, pasándole el valor 6 como argumento, y guardamos el resultado.
resultado = calcular_area_cuadrado(6)

# Paso 6: Mostramos el resultado en pantalla con un mensaje.
print("Área del cuadrado:", resultado) 

"""
	1.	Python llama a la función calcular_area_cuadrado(6).
	2.	Dentro de la función, se calcula:area = 6 * 6 → area = 36.
	3.	Luego, return area devuelve ese valor (36).
	4.	Ese valor se asigna a la variable resultado.
"""

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 1. Declaramos la función y le damos dos parámetros: ancho y alto
def calcular_Perimetro(ancho, alto):
    
    # 2. Calculamos el perímetro usando la fórmula del rectángulo
    perimetro = 2 * (ancho + alto)
    
    # 3. Devolvemos el resultado con return
    return perimetro

# 4. Llamamos la función con los valores 10 y 20, y guardamos el resultado en una variable
resultado = calcular_Perimetro(10, 20)

# 5. Imprimimos el resultado
print(f"Perimetro: {resultado}")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def Calcular_Area (base, altura): 
    area = base * altura
    return area #Devuelves ese resultado al lugar donde se llamó la función.(resultado)
resultado = Calcular_Area(10, 20) #Llamas a la función pasando los valores 10 y 20, y el resultado se guarda en la variable resultado.

print(f"El area es de {resultado}")

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def area_triangulo(base, altura): 
    area = (base * altura)/2
    return area
resultado = area_triangulo(15, 20) #Llamas a la función con los valores 15 y 20. El return regresa el resultado (150.0), y lo guardas en la variable resultado.
print(f"Area del triangulo {resultado}.")


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Primero pedimos al usuario que ingrese los grados en Celsius
entrada = input("Ingresa la temperatura en grados Celsius: ")
celsius = float(entrada)  # Convertimos la entrada a número

# Luego definimos la función
def celcius_farenheit(celsius): 
    conversor = (celsius * 9/5) + 32
    return conversor

# Llamamos a la función y mostramos el resultado
resultado = celcius_farenheit(celsius) #	2.	Guarda el resultado del return de esa función en la variable resultado.
print(f"{celsius}°C equivalen a {resultado}°F.")


#	•	Llamar a la función no es lo mismo que darle entrada.
#	•	El resultado no es solo para llamar, es para guardar lo que devuelve la función.

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 1. Solicitamos al usuario los tres valores separados por comas
entrada = input("Ingresa largo, ancho y alto separados por comas (ej. 10,5,2): ")

# 2. Separamos la cadena y convertimos cada parte a número flotante (float)
largo, ancho, alto = map(float, entrada.split(","))

# 3. Definimos una función que calcula el volumen de un prisma rectangular
def Calcular_Volumen(largo, ancho, alto): 
    volumen =  largo * ancho * alto
    return volumen  # 4. Devolvemos el volumen calculado

# 5. Llamamos a la función y guardamos el resultado en la variable 'resultado'
resultado = Calcular_Volumen(largo, ancho, alto)

# 6. Mostramos el resultado al usuario
print(f"Resultado: {resultado}")

#	1.	entrada.split(",") convierte la cadena "10,5,2" en una lista: ["10", "5", "2"].
#	2.	map(float, ["10", "5", "2"]) convierte cada cadena a número decimal (float):

