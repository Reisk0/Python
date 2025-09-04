""""
Mascota = input("Ingresa tu que tipo de mascota tienes: ").upper()
if (Mascota == "PERRO"):
    print(f"Tu mascota {Mascota.lower()}, es un perro muy lindo")
elif (Mascota != "Perro"):
    print(f"Tu mascota {Mascota}, no es un perro")
"""
"""
contador = 0
while True:
    entrada = int(input("Dime un número: "))
    
    if 5 <= entrada <= 100: 
        print(f"El número {entrada} está entre 5 y 100.")
    elif entrada < 1 or entrada > 100: 
        print(f"El número {entrada} está fuera de rango.")
    
    contador += 1  # ✅ Aumenta contador siempre
    
    terminar = input("¿Deseas ingresar otra cantidad? (si/no): ").lower()
    if terminar == "no":
        break

print(f"{contador} cantidades fueron ingresadas.")


if (not entrada > 0):
    print("Es mayor a 0.")
"""

#CUENTA LOS NUMERO POSITIVOS NEGATIVOS Y CEROS CON TRY Y EXCEPT
"""
positivo = 0
negativo = 0
cero = 0

while True:
    entrada = input("Ingrese una cantidad numérica (o 'fin' para salir): ")

    if entrada.lower() == "fin":
        break                   
                                # Aquí empieza un bloque try, que intenta convertir lo que escribió
                                # el usuario a un número entero (int).Si lo logra, guarda ese número
                                #  en la variable numero. Si no es un número válido (como “hola”), Python irá directo al bloque except.
    try:
        numero = int(entrada)

        if numero > 0:
            positivo += 1
        elif numero < 0:
            negativo += 1
        else:
            cero += 1

    except ValueError:
        print("❌ Entrada no válida. Por favor, ingresa un número o 'fin'.")    #Este bloque se ejecuta si ocurrió un error de conversión a entero 
                                                                                #(por ejemplo, si el usuario escribió “gato”)Se muestra un mensaje para indicar que la entrada no es válida.

print("\nResultados:")
print(f"Números positivos: {positivo}")
print(f"Números negativos: {negativo}")
print(f"Cantidad de ceros: {cero}")
"""

suma = 0
sumneg = 0
ceros = 0
datos_pos = 0  # Para contar los números positivos
datos_neg = 0  # Para contar los números negativos
while True:
    entrada = input("Ingresa una cantidad o si desea terminar escribe (fin): ")
    if entrada.lower() == "fin": 
        break
    try: 
        numero = int(entrada) 
        if numero > 0:
            suma += numero
            datos_pos += 1  # Contar positivos
        elif numero < 0: 
            sumneg += numero
            datos_neg += 1  # Contar negativos
        elif numero == 0: 
            ceros += 1  # Contar ceros
    except ValueError:
        print("Tipo de dato incorrecto, ingrese cantidades numéricas.")

# Imprimir los resultados finales
print("\nResultados finales:")
print(f"La cantidad de números positivos es: {datos_pos}, y su suma es: {suma}")
print(f"La cantidad de números negativos es: {datos_neg}, y su suma es: {sumneg}")
print(f"La cantidad de ceros ingresados es: {ceros}")

