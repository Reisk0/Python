SumaPositivos = 0  # Inicia la suma en 0

while True:  # Bucle infinito para pedir números hasta que el usuario decida parar
    entrada = input("Ingresa unicamente numeros positivos: ")  # Pide un número como texto
    numero = int(entrada)  # Convierte la entrada a número entero
    
    if numero == 0:  # Si el número es 0
        print("Numero ingresado cero, cerrando bucle: ")  # Mensaje de cierre
        break  # Sale del bucle
    
    if numero > 0:  # Si el número es positivo
        SumaPositivos += numero  # Lo suma a la variable
    
# Al salir del bucle, muestra la suma total
print(f"La suma de los numeros positivos es igual a {SumaPositivos}")