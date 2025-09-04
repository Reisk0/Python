
"""
🔧 Objetivo:
	•	Solicitar tres calificaciones con input()
	•	Convertirlas a float
	•	Crear una función con return para calcular el promedio
	•	Imprimir el resultado con un mensaje claro
	•	Validar que los datos sean correctos
"""

try:
    # 1. Pedimos las calificaciones
    entrada = input("Ingresa tres calificaciones separadas por comas, ejemplo (1,2,3): ")
    
    # 2. Separamos y convertimos a float
    cal_1, cal_2, cal_3 = map(float, entrada.split(","))

    # 3. Definimos la función para calcular el promedio
    def funcion(cal_1, cal_2, cal_3):
        operacion = (cal_1 + cal_2 + cal_3) / 3
        return operacion

    # 4. Llamamos a la función y guardamos el resultado
    promedio = funcion(cal_1, cal_2, cal_3)

    # 5. Mostramos el resultado formateado a 2 decimales
    print(f"Las calificaciones ingresadas son {cal_1}, {cal_2}, {cal_3}.")
    print(f"El promedio es de: {promedio:.2f}")

except ValueError:
    print("Tipo de dato inválido. Ingresa solo números, separados por comas.")