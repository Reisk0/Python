
"""
Objetivo: Mostrar todos los Pokémon cuyo nombre tenga más de 7 letras.
"""

Team_Pokemon = [
    {"No. PokeTeam": 1, "Nombre": "Riolu", "Combates": 15, "Naturaleza": "tranquila", "Puntos de experiencia": 9999 },  
    {"No. PokeTeam": 2, "Nombre": "Zoroark", "Combates": 150, "Naturaleza": "protectora", "Puntos de experiencia": 25077 }, 
    {"No. PokeTeam": 3, "Nombre": "Hydreigon", "Combates": 50, "Naturaleza": "Feroz", "Puntos de experiencia": 25041 }, 
    {"No. PokeTeam": 4, "Nombre": "Lycanrock", "Combates": 45, "Naturaleza": "Ozado", "Puntos de experiencia": 18995 }, 
    {"No. PokeTeam": 5, "Nombre": "Haxorus", "Combates": 60, "Naturaleza": "Protectora", "Puntos de experiencia": 19004 }, 
    {"No. PokeTeam": 6, "Nombre": "Darkrai", "Combates": 98, "Naturaleza": "Reservada", "Puntos de experiencia": 50457 }, 
]

# Definimos una función llamada 'Siete_Letras' que toma un Pokémon como argumento.
def Siete_Letras(pokemon): 
    # Retorna True si el nombre del Pokémon tiene más de 7 letras
    return len(pokemon["Nombre"]) > 7

# Usamos la función filter() para aplicar 'Siete_Letras' a cada Pokémon en la lista 'Team_Pokemon'
# Esto devolverá solo aquellos Pokémon que cumplen la condición (nombre con más de 7 letras)
Lista_Mas_d_siete = list(filter(Siete_Letras, Team_Pokemon))

# Verificamos si la lista tiene elementos (es decir, si encontró algún Pokémon con más de 7 letras)
if Lista_Mas_d_siete: 
    # Recorremos la lista filtrada y mostramos cada Pokémon que cumple con la condición
    for i in Lista_Mas_d_siete: 
        print(i)