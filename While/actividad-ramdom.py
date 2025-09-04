"""
calificacion = int(input("Ingresa tu ultima calificación: "))

if calificacion < 0 or calificacion > 100:
    print("Calificación fuera del rango")
elif calificacion < 60: 
    print("Insuficiente")
elif calificacion <= 69: 
    print("Suficiente")    
elif calificacion <= 79: 
    print("Buena")
elif calificacion <= 89:
    print("Muy Buena")
else:
    print("Excelente")
"""
#listas de datos
"""
pagos = [200, 400, 90]
pagos2 = [200, "pepe", 400]
print(pagos)
print(pagos[1])
print(pagos2[1])
"""    
#Diccionario
""""
diccinario = {
    "nombre": "juan", 
    "edad": 20, 
    "soltero": True
}
print(diccinario)
"""

#Casteo
"""
numero1 = "1"
numero2 = 2
print(int(numero1)+numero2)
"""

#Solicitud de contraseña
import time
import os

intentos = 0
max_intentos = 3

while True:
    if intentos == max_intentos: 
        print("Alcanzaste el número máximo de intentos. Acceso bloqueado.")
        break

    password = input("Ingrese la contraseña: ") 

    if password == "Python123": 
        print("¡Acceso concedido!")
        break
    else:
        intentos += 1
        print("Acceso denegado.")
        print(f"Número de intentos fallidos: {intentos}.")
        time.sleep(10)  # espera 10 segundos
        os.system('cls' if os.name == 'nt' else 'clear')  # limpia pantalla tanto para windows como para mac y linux
        