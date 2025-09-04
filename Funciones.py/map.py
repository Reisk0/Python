# 1 +++++++++++++++++++++++++++++++++++Logra que map suma una cantidad por si misma en una lista+++++++++++++++++++++++++++++++++++++++++++

# Definimos una función que suma un número consigo mismo
def suma(numero): 
    return numero + numero

# Usamos map para aplicar la función a cada elemento de la lista
resultado_suma = list(map(suma, [10, 110, 100]))

# Imprimimos el resultado: una lista con cada número sumado consigo mismo
print(resultado_suma)

# 2++++++++++++++++++++++++++++++++++++++logra que una frse se convierta en mayuscula+++++++++++++++++++++++++++++++++++++++++++++++++++

#version sin map
def mayus (palabra): 
    return palabra.upper()

funcion_mayusc = mayus("esta es una frase")

print(funcion_mayusc)

#version usando map
def mayus (palabra): 
    return palabra.upper()

frase = ["lista", "de", "palabras", "creadas."]
funcion_mayusc = list (map(mayus, frase))

print(funcion_mayusc)

#version frase de usuario

# Definimos una función llamada 'frase_usua' que recibe una variable 'entrada' (una cadena de texto)
# y devuelve esa misma cadena convertida a mayúsculas usando el método upper().
def frase_usua(entrada): 
    return entrada.upper()

# Solicitamos al usuario que ingrese una oración por teclado.
# Lo que escriba se almacenará en la variable 'oracion'.
oracion = input("ingresa una oracion: ")

# Llamamos a la función 'frase_usua' y le pasamos como argumento lo que el usuario escribió.
# El resultado (la frase en mayúsculas) se guarda en la variable 'llamar'.
llamar = frase_usua(oracion)

# Mostramos en pantalla el resultado, es decir, la oración transformada a mayúsculas.
print(llamar)


#++++++++++++++++++++++++++++++++++++ 🧠 Ejercicio: Elevar al cuadrado todos los números de una lista++++++++++++++++++++++++++++++++


# Definimos una función llamada 'cuadrado' que recibe un número y devuelve su cuadrado
def cuadrado (cantidad): 
    return cantidad * cantidad

# Creamos una lista de números que queremos transformar
lista_num = [10, 20, 5, 54, 50]

# Usamos 'map' para aplicar la función 'cuadrado' a cada número de la lista
# El resultado se convierte en una lista usando 'list()'
llamar_funcion = list(map(cuadrado, lista_num))

# Imprimimos el resultado final
print(f"numeros al cuadrado: {llamar_funcion}.")

#++++++++++++++++++++++++++++++++convertir todas las palabras a mayúsculas o contar cuántas letras tiene cada palabra.++++++++++++++++++++++

# Función que convierte una frase a mayúsculas
def mayus_contar(frase): 
    return frase.upper()  # Convierte la frase completa a mayúsculas

# Lista de frases (en vez de una sola frase como string)
frases = ["esta es una prueba", "otra frase corta", "map funciona bien"]

# Aplicamos map para convertir cada frase a mayúsculas
llamar_mayus_contar = list(map(mayus_contar, frases))

# Mostramos la lista resultante con las frases en mayúscula
print(f"Frases en mayúscula: {llamar_mayus_contar}")

# Contamos el número total de letras (sin contar espacios)
letras_totales = sum(len(frase.replace(" ", "")) for frase in frases)
print(f"Total de letras (sin contar espacios): {letras_totales}")