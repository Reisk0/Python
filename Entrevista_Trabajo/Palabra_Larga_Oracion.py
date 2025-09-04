# Pedimos al usuario que ingrese una oración
frase = input("Ingresa una oracion: ")

# Separamos la oración en palabras usando espacios como separador
separacion = frase.split()

# Inicializamos variables para guardar la palabra más larga y su longitud
palabra_larga = ""  
longitud = 0  

# Recorremos cada palabra de la lista
for letras in separacion:
    # Si la longitud de la palabra actual es mayor que la guardada
    if len(letras) > longitud:  
        palabra_larga = letras            # Actualizamos la palabra más larga
        longitud = len(palabra_larga)    # Actualizamos la longitud máxima

# Mostramos la palabra más larga y cuántos caracteres tiene
print(f"La palabra {palabra_larga} tiene {longitud} caracteres")
