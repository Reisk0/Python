
"""
	1.	Crea una función llamada celsius_a_fahrenheit que:
	•	Reciba como argumento un número (los grados Celsius).
	•	Devuelva el equivalente en grados Fahrenheit.
	2.	Luego:
	•	Pide al usuario que ingrese una temperatura en grados Celsius.
	•	Llama a tu función y muestra el resultado en pantalla.
"""
intentos = 0  # Se inicializa el contador de intentos

while True:  # Ciclo infinito que solo se rompe si se alcanza un intento válido o se exceden los intentos
    entrada = input("Ingresa temperatura en Celsius, lo convertiremos a Farenheit: ")
    intentos += 1  # Se suma 1 intento cada vez que se pide entrada
    print(f"Numero de intentos {intentos}")

    if intentos == 5: 
        print("Numero de intentos alcanzados.")
        break  # Se rompe el ciclo si ya se hicieron 5 intentos

    try:
        entrada_num = float(entrada)  # Se intenta convertir la entrada a número

        def Celcius_Faren(grados):  # Función para convertir a Fahrenheit
            return (grados * 9/5) + 32

        resultado = Celcius_Faren(entrada_num)  # Llamada a la función

        print(f"{entrada_num}° Centígrados equivalen a {resultado}° Farenheith.")
        break  # Salir del bucle si la entrada fue válida

    except ValueError:
        print("❌ Dato inválido. Por favor, ingresa solo números.")  # Mensaje si el valor no es un número