numerosPares = 0
numerosImpares = 0
multiplosDeCinco = 0
numerosNegativos = 0

while True:
    entrada = input("Ingresa una cantidad numerica (o escribe 'fin' para terminar): ")
    
    if entrada.lower() == "fin":
        break

    try: 
        numero = int(entrada)

        if numero % 2 == 0: 
            numerosPares += 1
        if numero % 2 != 0: # 👉 “Si el número no es divisible entre 2”,  funciona igual con positivos y negativos.
            numerosImpares += 1
        if numero % 5 == 0: 
            multiplosDeCinco += 1
        if numero < 0:
            numerosNegativos += 1

    except ValueError: 
        print("Tipo de dato invalido")

print("\nResultados finales:")
print(f"La cantidad de numeros pares es de: {numerosPares}.")
print(f"La cantidad de numeros impares es de: {numerosImpares}.")
print(f"La cantidad de numeros negativos es de: {numerosNegativos}.")
print(f"La cantidad de multiplos de cinco es de: {multiplosDeCinco}.")