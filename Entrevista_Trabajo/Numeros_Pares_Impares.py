# Creamos una lista con números del 1 al 10
Lista_Numeros = [1,2,3,4,5,6,7,8,9,10]

# Inicializamos una lista vacía para guardar los números pares
Num_Pares = []

# Inicializamos una lista vacía para guardar los números impares
Num_Nones = []

# Recorremos cada número de la lista Lista_Numeros
for num in Lista_Numeros: 
    # Si el número es divisible entre 2, es par
    if num % 2 == 0: 
        # Agregamos el número a la lista de pares
        Num_Pares.append(num)
    else: 
        # Si no es divisible entre 2, es impar y lo agregamos a la lista de impares
        Num_Nones.append(num)

# Imprimimos la lista de números pares
print("Números pares:", Num_Pares)

# Imprimimos la lista de números impares
print("Números impares:", Num_Nones)