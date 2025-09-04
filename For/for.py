
"""
for i in range(1, 26, 1): 
    if(i%2==0):
        print(i)
        """
"""
#MATCH revisar una condicion y hacer acciones dependiendo del resultado

numero = int(input("Ingresa una cantidad: "))

match numero: 
    case x if x >10:
        print("Es mayor a 10")
    case 1: 
        print("1")
    case _: 
        print("Es otra cosa")
    """
#Muestra los muneros del 1-5
for i in range(1, 6): 
    print(i)

#Muestra los numeros pares del 1-10
for i in range(1, 11): 
    if(i % 2 == 0): 
        print(f"Numeros pares del 1-10: {i}")
#Muestra multiplos de tres y sumalos al final. 
suma = 0
for i in range(1, 31): 
    if(i % 3 == 0):
        suma += i
        print(f"Multiplo de tres: {i}, \nResultados acumulado: {suma}.")
    
# Ingresa Calificaciones y calcula el promedio
suma = 0

for i in range(1, 6):
    calificacion = input(f"Ingresa calificación {i}: ")
    numero = int(calificacion)
    suma += numero

promedio = suma / 5
print(f"Promedio de calificaciones: {promedio}")

#Version con Try: 
"""
suma = 0
for i in range(1, 6):
    while True:
        calificacion = input(f"Ingresa calificación {i}: ")
        try:
            numero = int(calificacion)
            suma += numero
            break  # salir del while si todo fue bien
        except ValueError:
            print("❌ Ingresa un número válido.")

promedio = suma / 5
print(f"\n✅ Promedio de calificaciones: {promedio}")
"""
 #te amo bebo, eres el mejor y todas tus metas se haran realidad :3 es que este teclado no me gusta, pero me puedo acostumbrar a él, tal vez, solo tal vez, lo importante es que eres mi bubu especial y te amamre toda la vida :3

tabla = input("Ingresa un numero veras su tabla de multiplicacion: ")
for i in range(1, 11): 
    cantidad = int(tabla)
    cantidad *= i                                     
    print(f"Tabla de multiplicar = {cantidad}")