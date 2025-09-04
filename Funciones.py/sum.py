
"""
	1.	Crea una lista de números, por ejemplo: [2, 4, 6, 8]
	2.	Usa map() para obtener los cuadrados de cada número.
	3.	Usa sum() para sumar todos los cuadrados.
	4.	Imprime el resultado.
"""
# 😀 QUE SE VA A HACER
# Definimos una función que recibe un número y devuelve su cuadrado
def funcion_cuadrados(numeros): 
    return numeros * numeros    

# 😀 LISTA A LA QUE SE LO VAS A APLICAR
# Creamos una lista con varios números enteros
lista_numeros = [12, 2, 3, 5]

# 😀 AQUI SE LO APLICAS
# Usamos la función map() para aplicar 'funcion_cuadrados' a cada número de la lista
# Convertimos el resultado a lista para poder trabajar con él
llamar_funcion = list(map(funcion_cuadrados, lista_numeros))    

# 😀 MOSTRAR RESULTADO
# Mostramos los cuadrados y luego usamos sum() para sumar todos los valores
print(f"El cuadrado de las cantidades es: {llamar_funcion} y la suma de ellos es: {sum(llamar_funcion)}.")