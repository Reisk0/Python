
Team_Pokemon = [
    {"No. PokeTeam": 1, "Nombre": "Riolu", "Combates": 15, "Naturaleza": "tranquila", "Puntos de experiencia": 9999 },  
    {"No. PokeTeam": 2, "Nombre": "Zoroark", "Combates": 150, "Naturaleza": "protectora", "Puntos de experiencia": 25077 }, 
    {"No. PokeTeam": 3, "Nombre": "Hydreigon", "Combates": 50, "Naturaleza": "Feroz", "Puntos de experiencia": 25041 }, 
    {"No. PokeTeam": 4, "Nombre": "Lycanrock", "Combates": 45, "Naturaleza": "Ozado", "Puntos de experiencia": 18995 }, 
    {"No. PokeTeam": 5, "Nombre": "Haxorus", "Combates": 60, "Naturaleza": "Protectora", "Puntos de experiencia": 19004 }, 
    {"No. PokeTeam": 6, "Nombre": "Darkrai", "Combates": 98, "Naturaleza": "Reservada", "Puntos de experiencia": 50457 }, 
]
while True:
    entrada = input("Nombre del Pokémon: ")
    
    for pokemon in Team_Pokemon:
        if pokemon["Nombre"].lower() == entrada.lower():
            print(f"Información de Pokémon: {pokemon}")
            break
    else:
        print("Pokemon no encontrado, ingresa otro nombre: ")
        continue  # vuelve a pedir el nombre

    break  # sale del while si se encontró
    