# Pedimos al usuario que escriba su edad; la entrada será un texto
entrada = input("Ingresa tu edad: ")

# Iniciamos un ciclo infinito para validar que la entrada sea numérica
while True: 
    try: 
        # Intentamos convertir la entrada a un número entero
        edad_num = int(entrada)

        # Definimos una función llamada 'edad' que recibe un número (edad) como parámetro
        def edad(edad): 
            # Si la edad es exactamente 18, devolvemos un mensaje especial
            if edad == 18: 
                return "Tienes 18 años"
            # Si la edad es mayor a 18, devolvemos otro mensaje
            elif edad > 18: 
                return "Tienes + de 18 años"
            # Si la edad es menor a 18, devolvemos un mensaje distinto
            else: 
                return "Tienes - de 18 años"
        
        # Llamamos a la función pasando la edad como argumento y guardamos el resultado
        llamar_funcion = edad(edad_num)

        # Mostramos el mensaje combinado con la edad numérica ingresada
        print(f"el usuario tiene {edad_num}, {llamar_funcion}")

        # Como todo salió bien, salimos del ciclo con 'break'
        break

    # Si ocurre un error al convertir el texto a número, lo manejamos aquí
    except ValueError: 
        print("Ingresa solo cantidades numericas")

        """
    •	return envía un resultado desde la función hacia quien la llamó.
	•	Ese resultado puede ser texto, número, lista, booleano, etc.
	•	Puedes guardarlo en una variable para usarlo después, o imprimirlo directamente.
        """