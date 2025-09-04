"""
👉 Ahora vamos a mejorar el ejercicio:

Quiero que escribas un programa en Python que pida 5 números al usuario y al final:
	1.	Muestre la suma total de esos números.
	2.	Muestre el número más grande.
	3.	Muestre el número más pequeño.
"""

try: 
            entrada = input("Ingresa cinco numeros, (ejemplo: 1,2,3,4,5)")
            numeros = entrada.split(",")
            numero_entero = int(numeros)
        
            lista_num = []
            max_num = max(numero_entero)
            min_num = min(numero_entero)
            sum_num = sum(numero_entero)

            for N in range(1, numero_entero): 
                lista_num.append(N)

except ValueError: print("Dato invalido.")

print(f"Lista: {lista_num}")
print(f"Numero Mayor: {max_num}")
print(f"Numero Menor: {min_num}")
print(f"Suma de lista: {sum_num}")