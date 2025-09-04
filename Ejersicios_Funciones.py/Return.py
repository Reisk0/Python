# Definimos una función llamada CalcularArea que recibe un parámetro llamado 'lado'
# y que devuelve un entero (int). Esto lo indicamos con -> int (anotación de tipo).
def CalcularArea(lado) -> int:
    area = lado * lado  # Calculamos el área del cuadrado (lado * lado)
    return area  # Retornamos el resultado al lugar donde se llamó la función

# Pedimos al usuario que ingrese el valor de un lado del cuadrado
lado_input = input("Ingresa el lado del cuadrado: ")

# Convertimos ese valor de texto (string) a número entero (int)
lado_input = int(lado_input)

# Llamamos a la función CalcularArea, pasando como argumento el valor ingresado por el usuario
resultado = CalcularArea(lado_input)

# Imprimimos el resultado que nos devolvió la función
print(resultado)