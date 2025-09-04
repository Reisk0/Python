# Bucle infinito para permitir intentos hasta que el nombre sea válido
while True: 

    # Pedimos al usuario que ingrese un nombre de usuario
    entrada = input("Ingresa un nombre de usuario: ")

    # Variables para verificar si contiene al menos un número, una letra y si inicia con letra
    tiene_numero = False
    tiene_letra = False
    inicia_mayus = False

    # Recorremos cada letra del nombre ingresado
    for letra in entrada: 
        # Verificamos si hay al menos un número
        if letra.isdigit():
            tiene_numero = True
        # Verificamos si hay al menos una letra
        if letra.isalpha():
            tiene_letra = True
        
    # Verificamos si el primer caracter es una letra y empieza con mayuscula
    if entrada[0].isupper():
        inicia_mayus = True

    # Función para validar si el nombre cumple con todos los requisitos
    def validar_usuario(usuario): 
        if len(usuario) >= 6 and tiene_letra == True and tiene_numero == True and inicia_mayus == True: 
            return True  # El nombre es válido
        else: 
            return False  # El nombre no cumple con las reglas

    # Si la función devuelve True, damos la bienvenida y salimos del bucle
    if validar_usuario(entrada) == True:
        print(f"Nombre de usuario valido, bienvenido {entrada}.")
        break
    else:
        # Si no es válido, se le avisa al usuario y se repite el ciclo
        print(f"nombre de usuario {entrada} invalido, trata de nuevo.")    