#Tabla de multiplicar
tabla = input("Ingresa un número para ver su tabla de multiplicación: ")
cantidad = int(tabla)

for i in range(1, 11):
    resultado = cantidad * i
    print(f"{cantidad} x {i} = {resultado}")

#Suma los numeros impares hasta llegat al 100

total = 0
for i in range(1, 101): 
    if(i % 2 == 1):
        total += i
print(f"La suma total de los numeros impares del 1 al 100 es: {total}")

# Suma los numeros que son multiplos de tres cinco o ambos:
multiplo_tres = 0
multiplo_cinco = 0
multiplo_ambos = 0
for i in range(1, 51):
    if(i % 3 == 0): 
        multiplo_tres += i
    if(i % 5 == 0): 
        multiplo_cinco += i
    if (i % 3 == 0 and i % 5 == 0): 
        multiplo_ambos += i
    
print(f"Multiplos de 3: {multiplo_tres}")
print(f"Multiplos de 5: {multiplo_cinco}")
print(f"Multiplos de ambos: {multiplo_ambos}")

#Conteo con ciclo for
positivo = 0
negativo = 0
ceros = 0
pares = 0
impares = 0

for i in range(1, 6):
    entrada = input(f"Ingrese cantidad numérica {i}: ")
    numeral = int(entrada)

    # Primero clasificamos el número
    if numeral > 0:
        positivo += 1
    elif numeral < 0:
        negativo += 1
    else:
        ceros += 1  # solo si es exactamente 0

    # Ahora evaluamos par o impar
    if numeral % 2 == 0:
        pares += 1
    else:
        impares += 1

# Resultados
print(f"Positivos: {positivo}.")
print(f"Negativos: {negativo}.")
print(f"Ceros: {ceros}.")
print(f"Pares: {pares}.")
print(f"Impares: {impares}.") 

