"""Suma de dos Variables 
def suma():
    a = 1
    b = 2
    print(f"La suma de a y b es = {a + b}")
suma()"""

"""#Suma de dos inputs
a = int(input("Ingresa la primera cantidad: "))
b = int(input("Ingresa la segunda cantidad: "))

def suma():
    return a + b
print(f"La suma de las cantidades es: {suma()}")"""

#Numero 100 if esle elif
"""
a = int(input("Ingresa una cantidad: "))
def mayor():
    if a > 100:
        print(f"el numero {a} es mayor a 100.")
    elif a == 100:
        print("El numero es igual a 100")
    else: 
        print("la cantidad es menor a 100.")
mayor()"""

#Comparar dos numeros
"""
a = int(input("Ingresa la primera cantidad: "))
b = int(input("Ingrese la segunda cantidad: "))

def comparacion(): 
        if a > b: 
           print(f"el numero {a} es mayor a {b}.")
        elif a == b: 
            print(f"{a} y {b} equivalen a lo mismo.") 
        elif a < b: 
            print(f"el numero {b} es mayor a {a}.")
comparacion()"""


#Compara 3 numeros, cual es el mayor ?

a = int(input("Ingresa la primera cantidad: "))
b = int(input("Ingresa la segunda cantidad: "))
c = int(input("Ingresa la tercera cantidad: "))

def comparacion(): 
    if a == b == c:
        print("Los tres números son iguales.")
    elif a == b or a == c or b == c:
        print("Hay al menos dos números iguales.")
    elif a > b and a > c: 
        print(f"El número {a} es mayor que {b} y {c}.")
    elif b > a and b > c: 
        print(f"El número {b} es mayor que {a} y {c}.")
    elif c > a and c > b: 
        print(f"El número {c} es mayor que {a} y {b}.")

comparacion()