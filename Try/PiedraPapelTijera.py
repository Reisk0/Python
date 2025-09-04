# random.choice genera una eleccion aletoria

import random

# Lista de opciones
opciones = ["piedra", "papel", "tijera"]
rival = random.choice(opciones)

# Elección del usuario
usuario = input("Es hora de jugar! Elige piedra, papel o tijera: ").lower()

# Mostrar elección del rival
print(f"El rival eligió: {rival}")

# Determinar el ganador
if usuario == rival:
    print("¡Es un empate!")
elif usuario == "piedra":
    if rival == "tijera":
        print("¡Ganaste! Piedra vence a tijera.")
    else:
        print("¡Perdiste! Papel vence a piedra.")
elif usuario == "papel":
    if rival == "piedra":
        print("¡Ganaste! Papel vence a piedra.")
    else:
        print("¡Perdiste! Tijera vence a papel.")
elif usuario == "tijera":
    if rival == "papel":
        print("¡Ganaste! Tijera vence a papel.")
    else:
        print("¡Perdiste! Piedra vence a tijera.")
else:
    print("Opción no válida. Intenta de nuevo.")