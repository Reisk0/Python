


while True:
    cantidad = int (input("Ingresa un numero positivo"))
    if cantidad > 0: 
        print("el numero es positivo: ")
    else: 
        print("el numero es negativo: ")

    salir = input("¿Quieres salir? (s/n): ")
    if salir.lower() == "s":
        break

