#Creando un clasificador de indice de masa corporal
while True:
    try:
        datos = input("Ingresa tu peso en Kg y tu estatura en cm separados por comas (ejemplo: 70,170): ")
        peso, estatura = map(float, datos.split(","))

        def calcular_IMC(peso, estatura_cm): # aqui renombramos el argumento de la entrada para que sea mas entendible, recuerdad que la funcion toma el valor en base a la posicion que e asignas al principio.
            estatura_m = estatura_cm / 100  # Convertimos centímetros a metros
            imc = peso / (estatura_m ** 2)
            return imc

        IMG = calcular_IMC(peso, estatura)

        print(f"Estatura = {estatura}cm, Peso = {peso}kg.")
        
        if IMG < 18.5:
            print(f"Tu IMC es de {IMG:.2f}, Clasificación: Bajo peso.")
        elif 18.5 <= IMG <= 24.9:
            print(f"Tu IMC es de {IMG:.2f}, Clasificación: Normal.")
        elif 25 <= IMG <= 29.9:
            print(f"Tu IMC es de {IMG:.2f}, Clasificación: Sobrepeso.")
        elif IMG >= 30:
            print(f"Tu IMC es de {IMG:.2f}, Clasificación: Obesidad.")
        break
    except ValueError:
       print("Dato inválido. Ejemplo válido: 70,170 (peso en kg, estatura en cm). Inténtalo de nuevo.")