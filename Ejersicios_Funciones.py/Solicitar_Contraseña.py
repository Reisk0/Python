"""
📌 Crea una función llamada verificar_contrasena que reciba una contraseña (cadena de texto) 
y devuelva un mensaje indicando si es segura o no.
"""

# Inicia ciclo infinito hasta que el usuario escriba una contraseña segura
while True:
    entrada = input("Ingresa una contraseña: ")

    # Variables de control para saber si hay mayúscula y número
    tiene_mayuscula = False
    tiene_numero = False   

    # Recorremos cada letra de la contraseña
    for letra in entrada: 
        if letra.isupper():
            tiene_mayuscula = True
        if letra.isdigit():
            tiene_numero = True

    # Función que verifica si la contraseña es segura
    def password(contraseña): 
        if len(contraseña) >= 8 and tiene_mayuscula and tiene_numero: 
            return True  # Devuelve True si es segura
        else: 
            return False  # Devuelve False si no lo es

    # Llamamos la función y evaluamos el resultado
    if password(entrada): #“Si la función devolvió True (es segura), imprime el mensaje y termina el programa.”
        print("✅ La contraseña es segura. Bien hecho.")
        break  # Salimos del ciclo si fue segura
    else:
        print("❌ La contraseña no es segura. Intenta nuevamente.\n")


