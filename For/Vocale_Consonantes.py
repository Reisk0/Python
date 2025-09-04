# Creamos un contador para las vocales
vocales = 0

# Creamos un contador para las consonantes
consonantes = 0

# Solicitamos al usuario que escriba una frase y la convertimos a minúsculas
frase = input("Ingresa una frase, contaremos las vocales y consonantes: ").lower()

# Iniciamos un ciclo for para recorrer cada letra en la frase
for letra in frase: 
    # Si la letra es una vocal (está en la cadena 'aeiou')
    if letra in "aeiou":
        vocales += 1
    # Si la letra es una letra del alfabeto pero NO es una vocal (es consonante)
    elif letra.isalpha(): #para verificar si es una letra (y no contar espacios o símbolos como consonantes).
        consonantes += 1
    # Si no es ni vocal ni consonante (por ejemplo, espacio o número), no hacemos nada

# Mostramos los resultados
print(f"{frase} contiene {vocales} vocales y {consonantes} consonantes.")