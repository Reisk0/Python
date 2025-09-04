# Pedimos al usuario que ingrese números separados por coma
entrada = input("Ingresa varios números separados por comas (ej. 5,-2,0,8): ")

# Variables para conteo y suma
ceros = 0
positivos = 0
negativos = 0
suma = 0

# Convertimos la entrada en una lista, dividiendo por comas
lista = entrada.split(",")

# Creamos una nueva lista para guardar los números válidos convertidos a enteros
numeros = []

# Recorremos cada elemento ingresado
for valor in lista:
    try:
        numero = int(valor.strip())  # Convertimos a entero, eliminando espacios
        numeros.append(numero)  # Guardamos en la lista original

        if numero == 0:
            print("Número cero ingresado.")
            ceros += 1
        elif numero > 0:
            print("Número positivo.")
            positivos += 1
        else:
            print("Número negativo.")
            negativos += 1

        suma += numero  # Sumamos todos los números

    except ValueError:
        print(f"'{valor}' no es un número válido, se ignora.")

# Mostramos los resultados
print(f"\nLista original: {numeros}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Ceros: {ceros}")
print(f"Suma total: {suma}")