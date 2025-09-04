
resultados = 0
frias = 0
templadas = 0
calurosas = 0

while True:
    entrada = input("Ingresa una temperatura (o escribe fin para terminar):")
    if entrada == "fin":
        break
    try:
        temperatura = int(entrada)
        if temperatura < 10: 
            frias += 1
        elif 10 <= temperatura <= 25: #para verificar si un número está entre dos valores
            templadas += 1
        elif temperatura > 25: 
            calurosas += 1
    except ValueError: print("Ingrese unicamente datos numericos. ")

print("\nResultados finales:")
print(f"Frias: {frias}.")
print(f"Calurosas: {calurosas}.")
print(f"Templadas: {templadas}.")