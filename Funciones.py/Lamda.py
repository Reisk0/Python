
print (max ([1,2,3,4,5,6,7,24]))
print (min([1233,43,42,566,2,1]))


#++++++++++++++++++++++++++++++++++++++++++++++++++Modulo Operator+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
#operaciones sencillas dentro de python

import operator as op #import {libreria} as apodo

print(op.add(10,5)) #add se maneja como sumar dos valores
print(op.mul(10,5)) #mul se maneja como sumar dos valores
print(op.pow(10,5)) #pow eleva a a la potenci de b
print(op.eq("hola","hola")) #a == b ?



#+++++++++++++++++++++++++++++++++++++++++++++++++++Funciones puras en impuras+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def multiplicar(a,b): 
    return a*b #funcion pura, no altera el exterior


import math
def sumar(a, funcion):
    return a + funcion(a)

def cuadrado(a):
    return a*a

def raiz(a): 
    return math.sqrt(a) 

def cubo(a): 
    return math.pow(a,3)

print(sumar (10, cubo))

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Definimos una función llamada 'fn' que eleva un número al cubo
def fn(a): 
    return a**3  # Es equivalente a: a * a * a

# Definimos una segunda función llamada 'fn2' que eleva un número al cuadrado
def fn2(a): 
    return a**2  # Es equivalente a: a * a

# Creamos una función anónima (lambda) y la guardamos en una variable llamada 'funcion_lambda'
# Esta función toma dos argumentos:
# - x: un número
# - funcion: una función que se le aplicará a x
# Luego devuelve la suma de x + funcion(x)
funcion_lambda = lambda x, funcion: x + funcion(x)

# También definimos lo mismo que arriba, pero con la sintaxis tradicional
# Esta función se llama 'funcion2', hace lo mismo que 'funcion_lambda'
def funcion2(x, funcion): 
    return x + funcion(x)

# Ahora llamamos a la función 'funcion_lambda' pasándole:
# - 50 como valor de x
# - la función 'fn' como argumento de función
# Es decir, se ejecuta: 50 + fn(50) => 50 + (50^3) => 50 + 125000 => 125050
resultado1 = funcion_lambda(50, fn)
resultado2 = funcion_lambda(45, fn2)

# Mostramos el resultado en pantalla
print(resultado1)  # Imprime: 125050


#++++++++++++++++++++++++++++++++++++++++caso practic lambda+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Función que multiplica el promedio por 10 (para apoyo alto)
def calcular_apoyo_alto(promedio):
    return promedio * 10

# Función que multiplica el promedio por 5 (para apoyo medio)
def calcular_apoyo_medio(promedio):
    return promedio * 5

# Función que multiplica el promedio por 2.5 (para apoyo bajo)
def calcular_apoyo_bajo(promedio):
    return promedio * 2.5

# Función que recibe un número y una función para calcular el apoyo
def mostrar_apoyo(numero, funcion):
    resultado = f"El promedio de {numero} es {funcion(numero)}% en su inscripción."
    return resultado  # ← se devuelve el resultado, no se imprime directamente

# Bucle para pedir calificaciones y mostrar apoyos según el rango
while True:
    input_calificacion = input("Escribe tu calificación para calcular tu beca (0 para salir): ")
    
    if input_calificacion.isdigit():
        calificacion = int(input_calificacion)
        
        # Salida si el usuario pone 0
        if calificacion == 0:
            print("Saliendo del programa.")
            break
        
        # Verifica si está en el rango válido
        if 1 <= calificacion <= 10:
            # Aplica según el valor
            if calificacion > 7:
                print(mostrar_apoyo(calificacion, calcular_apoyo_alto))
            elif calificacion > 5:
                print(mostrar_apoyo(calificacion, calcular_apoyo_medio))
            else:
                print(mostrar_apoyo(calificacion, calcular_apoyo_bajo))
        else:
            print("Por favor, ingresa una calificación válida del 1 al 10.")
    else:
        print("Por favor, ingresa un número válido.")