diccionario = {}

for clave in range(1, 6): 
    entrada = input("Ingresa una palabra que no contenga x: ").lower()

    if "x" in entrada:
        print("La palabra contiene una X, dato inválido.")
    else: 
        # dictio     key      value
        diccionario[clave] = entrada

print(f"El diccionario es: {diccionario}")