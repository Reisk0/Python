


import random
numeroSecreto = random.randint(1, 10) #Asi es como se genera un numero aleatorio
intentos = 0 
Maxintentos = 5
while True:
    numeroUsuario = int(input("Ingresa una cantidad entre 1 y 10: "))
    intentos += 1  # <-- Esto es importante

    if numeroUsuario == numeroSecreto: 
        print(f"Felicidades, adivinaste el número secreto es: {numeroSecreto}.")
        break
    elif numeroUsuario < numeroSecreto:
        print("El numero es mayor. Intenta otra vez.")
    elif numeroUsuario > numeroSecreto:
        print("El numero es menor. Intenta otra vez.")
        
    if intentos == Maxintentos: 
        print("Alcanzaste el numero maximo de intentos")
        break