# Lista de números del 1 al 10 que queremos evaluar
lista_Numeros = [1,2,3,4,5,6,7,8,9,10]

# Recorremos cada número de la lista
for num in lista_Numeros:
    # Caso especial: los números menores a 2 (0 y 1) NO son primos
    if num < 2:
        print(f"{num} NO es primo")
    else:
        # Suponemos que el número es primo (lo comprobamos más adelante)
        es_primo = True

        # Recorremos todos los posibles divisores desde 2 hasta num-1
        for i in range(2, num):  
            # Si encontramos un divisor exacto (residuo 0), entonces no es primo
            if num % i == 0:
                es_primo = False  # Marcamos que no es primo
                break             # Terminamos el ciclo porque ya no hace falta seguir probando

        # Si después del ciclo la variable es_primo sigue en True, significa que sí es primo
        if es_primo:
            print(f"{num} es primo")
        else:
            print(f"{num} NO es primo")