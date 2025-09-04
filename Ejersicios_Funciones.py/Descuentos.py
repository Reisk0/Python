"""
Vas a crear un programa que:
	1.	Pida al usuario el precio original de un producto.
	2.	Pida el porcentaje de descuento que se le aplicará.
	3.	Calcule el precio final con descuento usando una función.
	4.	Muestre el resultado con claridad.
"""
while True:  # Bucle para seguir preguntando si quiere calcular otro producto
    while True:  # Bucle de validación del input
        try:
            entrada = input("Ingresa el precio y el descuento (ej. 100,20): ")
            precio, descuento = map(float, entrada.split(","))
            break  # Salimos del bucle interno si los datos son correctos
        except ValueError:
            print("Formato inválido. Asegúrate de usar coma y solo números.")

    # Función para calcular el descuento
    def funcion_descuento(precio, descuento):
        return precio - (precio * descuento / 100)

    resultado = funcion_descuento(precio, descuento)

    print(f"\nPrecio original: ${precio}")
    print(f"Descuento: {descuento}%")
    print(f"Precio final con descuento: ${resultado}\n")

    # Preguntamos al usuario si desea continuar
    seguir = input("¿Deseas calcular otro descuento? (sí/no): ").strip().lower()
    if seguir != "sí":
        print("Gracias por usar el programa. ¡Hasta luego!")
        break  # Salimos del bucle principal si no quiere continuar