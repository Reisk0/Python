import random  # Importamos el módulo 'random' para generar números aleatorios

Intentos = 0  # Contador de intentos que ha hecho el jugador

# Generamos un número aleatorio entre 1 y 10 (incluidos ambos)
NumeroSecreto = random.randint(1, 10)

# Iniciamos un bucle que se repetirá hasta que el jugador acierte
while True:
    try:
        # Pedimos al jugador que ingrese un número
        entrada = input("Trata de adivinar el número (entre 1 y 10): ")
        
        # Convertimos la entrada a número entero
        numero = int(entrada)
        
        # Aumentamos el contador de intentos
        Intentos += 1

        # Comparamos la entrada del usuario con el número secreto
        if numero > NumeroSecreto:
            print("El número es mayor al número secreto, intenta con uno más pequeño.")
        elif numero < NumeroSecreto:
            print("El número es menor al número secreto, intenta con uno más grande.")
        else:
            # Si el número es correcto, mostramos el mensaje y salimos del bucle
            print(f"¡Acertaste! El número secreto es: {NumeroSecreto}")
            print(f"Número de intentos: {Intentos}")
            break  # Salimos del bucle
    except ValueError:
        # Si el jugador no escribe un número válido, mostramos este mensaje
        print("Eso no es un número válido, intenta de nuevo.")

        