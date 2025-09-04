

num_ingre = 0
suma_pos = 0
suma_neg = 0
conteo_pos = 0
conteo_neg = 0
ceros = 0

while True: 
    cantidad = input("Ingresa una cantidad numerica o escribe fin para terminar: ")   
    
    if cantidad.lower() == "fin":
        break

    try: 
        numero = int(cantidad)
        num_ingre += 1

        if numero > 0:
            suma_pos += numero
            conteo_pos += 1
        elif numero < 0: 
            suma_neg += numero
            conteo_neg += 1
        elif numero == 0:
            ceros += 1
    except ValueError:
        print("Tipo de dato invalido, ingresa cantidades numericas.")

# Cálculo de promedios (evitar división por cero)
promedio_pos = suma_pos / conteo_pos if conteo_pos > 0 else 0
promedio_neg = suma_neg / conteo_neg if conteo_neg > 0 else 0

print("\nResultados finales:")
print(f"Cantidad total de datos numéricos ingresados: {num_ingre}")
print(f"Cantidad de ceros ingresados: {ceros}")
print(f"Promedio de los números positivos: {promedio_pos}")
print(f"Promedio de los números negativos: {promedio_neg}")