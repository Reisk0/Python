
palabra = input("Ingresa una frase, verificaremos si es un palindromo: ").lower().replace(" ", "")

if palabra == palabra[::-1]: 
        print(" la pabra es un palindromo")
else: 
        print("la frase no es un palindromo")


coinci = 0  # Inicia el contador de coincidencias en 0

frase = input("Ingresa una frase: ").lower()  # Pide la frase y la convierte a minúsculas
coincidencia = input("Elige una palabra, veremos cuántas veces se repite: ")  # Pide la palabra a buscar

palabras = frase.split()  # Divide la frase en una lista de palabras

for ciclo in palabras:  # Recorre cada palabra de la lista
    if coincidencia == ciclo:  # Si la palabra ingresada coincide con la palabra de la lista
        coinci += 1  # Aumenta el contador

print(f"La palabra '{coincidencia}' se repite un total de {coinci} veces.")  # Muestra el resultado


# +++++++++++++++++++++++++++++++++++Este es el uso correcto del split()++++++++++++++++++++++++++++++++++++++++++++++++
frase = input("Ingresa una frase: ")
resultado = frase.split()
print(resultado)

contador = 0
entrada = input("Ingresa una frase, contaremos cuantas palabras tiene esta oracion: ").lower()

frase = entrada.split()
for ciclo in frase: 
      contador += 1
print(f"la cantidad de palabras en la oracion es de {contador}")