
ListaDeNumeros = []
NumerosImpares = 0
for ciclo in range(5): 
        entrada = input("Ingresa Numeros enteros: ")
        try: 
            numero = int(entrada) 
            if numero % 2 == 1:
                print("numero impar.")
                NumerosImpares += 1
            else: 
                ListaDeNumeros.append(numero)

        except ValueError:
            print("Tipo de dato invalido, trata de nuevo")

print(F"Lista de numeros pares {ListaDeNumeros}.")
print(F"Numero impares Ingresados: {NumerosImpares}.")