
entrada = input("Ingresa varias edades separadas por comas, ejemplo: (10, 22, 5, 80): ").split(",")


lista_Edades = []
Menor = 0
Adulto = 0
Adulto_Mayor = 0

try: 
    for edad in entrada:
        numero_cantidades = +1
        lista_Edades.append(edad)
    edad_numero = int(edad.strip())
    if (edad_numero < 18): 
        Menor =+ 1
    elif 18 <= edad_numero <= 59:
        Mayor =+ 1
    elif(edad_numero > 60 ): 
        Mayor =+ 1
except ValueError: 
    print("Ingresa solo cantdidades numericas")

print(f"Edades Ingresadas: {lista_Edades}.")
print(f"Menores de edad: {Menor}.")
print(f"Aldultos de edad: {Adulto}.")
print(f"Adultos Mayores de edad: {Adulto_Mayor}.")
print(f"Mayores de edad: {numero_cantidades}")