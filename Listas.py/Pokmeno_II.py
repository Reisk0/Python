

Team_Pokemon = [
    {"No. PokeTeam": 1, "Nombre": "Riolu", "Combates": 15, "Naturaleza": "tranquila", "Puntos de experiencia": 9999 },  
    {"No. PokeTeam": 2, "Nombre": "Zoroark", "Combates": 150, "Naturaleza": "protectora", "Puntos de experiencia": 25077 }, 
    {"No. PokeTeam": 3, "Nombre": "Hydreigon", "Combates": 50, "Naturaleza": "Feroz", "Puntos de experiencia": 25041 }, 
    {"No. PokeTeam": 4, "Nombre": "Lycanrock", "Combates": 45, "Naturaleza": "Ozado", "Puntos de experiencia": 18995 }, 
    {"No. PokeTeam": 5, "Nombre": "Haxorus", "Combates": 60, "Naturaleza": "Protectora", "Puntos de experiencia": 19004 }, 
    {"No. PokeTeam": 6, "Nombre": "Darkrai", "Combates": 98, "Naturaleza": "Reservada", "Puntos de experiencia": 50457 }, 
]
#++++++++++++++++++++Filtra los Pokemon con mas de 50 combates++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Definimos una función llamada 'combates' que recibe un diccionario llamado 'pokemon'
# Esta función revisa si el número de combates del Pokémon es mayor a 50
def combates(pokemon): 
    return pokemon["Combates"] > 50  # Retorna True si tiene más de 50 combates, si no, retorna False

# 'filter' es una función integrada de Python que filtra elementos de una colección
# En este caso, aplica la función 'combates' a cada elemento de la lista 'Team_Pokemon'
# Solo los Pokémon para los que 'combates(pokemon)' sea True se mantienen
llamar_funcion = list(filter(combates, Team_Pokemon))  
# Convertimos el resultado a una lista porque filter devuelve un objeto iterable (no una lista directamente)

# Imprime la lista de Pokémon que tienen más de 50 combates
print(llamar_funcion)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
Objetivo:
Pide al usuario que ingrese una naturaleza (por ejemplo: "protectora") 
Muestra todos los Pokémon del equipo que tengan esa naturaleza (sin importar mayúsculas o minúsculas).
"""
# Se solicita al usuario que ingrese una naturaleza (como "feroz", "protectora", etc.)
# El método .lower() convierte la entrada a minúsculas para que la comparación sea insensible a mayúsculas
entrada = input("Ingresa una naturaleza: ").lower()

# Se crea una lista vacía donde se guardarán los Pokémon que coincidan con la naturaleza ingresada
encontrados = []

# Se recorre cada Pokémon en la lista Team_Pokemon
for PM in Team_Pokemon:
    # Se compara la naturaleza del Pokémon (convertida a minúsculas) con la entrada del usuario
    if PM["Naturaleza"].lower() == entrada:
        # Si hay coincidencia, se agrega ese Pokémon a la lista 'encontrados'
        encontrados.append(PM)

# Si la lista 'encontrados' tiene al menos un Pokémon, se ejecuta este bloque
if encontrados:
    print("Pokémon encontrados:")
    # Se recorre la lista 'encontrados' e imprime uno por uno
    for pokemon in encontrados: #aqui recorres la lista de encotrados
        print(pokemon)#con esto imprimos los pokemon dentro de la lista de encotrados
# Si no se encontró ningún Pokémon con esa naturaleza, se ejecuta este otro bloque
else:
    print("No se encontraron Pokémon con esa naturaleza.")


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++USANDO FILTER+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Se solicita al usuario que escriba una naturaleza. 
# La función .lower() convierte la entrada a minúsculas para hacer la comparación sin importar mayúsculas o minúsculas.
entrada = input("Ingresa una naturaleza: ").lower()

# Se define una función llamada 'misma_naturaleza' que tomará un Pokémon (diccionario) como argumento.
# Esta función compara si la naturaleza del Pokémon (también en minúsculas) es igual a la que ingresó el usuario.
def misma_naturaleza(p):
    return p["Naturaleza"].lower() == entrada

# Se utiliza la función 'filter' para aplicar la función 'misma_naturaleza' a cada Pokémon dentro de la lista Team_Pokemon.
# 'filter' devuelve un objeto con los elementos que cumplen la condición (es decir, los Pokémon con la misma naturaleza).
# Luego, convertimos ese resultado en una lista utilizando 'list()'.
resultado = list(filter(misma_naturaleza, Team_Pokemon))

# Se evalúa si la lista 'resultado' contiene al menos un elemento (Pokémon encontrado).
# En Python, una lista vacía se considera False, y una lista con elementos se considera True.
if resultado:
    # Si hay Pokémon en la lista resultado, se muestra este mensaje.
    print("Pokémon encontrados:")
    
    # Se recorre cada Pokémon encontrado y se imprime su información completa (como un diccionario).
    for pokemon in resultado:
        print(pokemon)
else:
    # Si no se encontró ningún Pokémon con esa naturaleza, se muestra este mensaje.
    print("No se encontraron Pokémon con esa naturaleza.")