
NumeroDePersonas = 0
MenoresDeEdad = 0
MayoresDeEdad = 0
Nonatos = 0

while True:
    entrada = input("Ingresa una edad, si deseas terminar escribre fin: ")
    if entrada.lower() == "fin": 
        break
    try: 
        numero = int(entrada)
        NumeroDePersonas += 1
        if numero < 0:
            Nonatos += 1
        elif numero < 18:
            MenoresDeEdad += 1
        else:
            MayoresDeEdad += 1
    except ValueError:
        print("Informacion ingresada invalida.")

print("\n Resultados:")
print(f"Cantidad de edad ingresadas {NumeroDePersonas}.")
print(f"Cantidad de personas mayores de edad {MayoresDeEdad}.")
print(f"Cantidad de personas menores de edad {MenoresDeEdad}.")
print(f"Cantidad de sin nacer {Nonatos}.")