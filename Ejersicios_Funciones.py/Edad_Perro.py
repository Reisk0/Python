# Pedimos al usuario que ingrese la edad de su mascota y la guardamos como texto
entrada = input("Ingresa la edad de tu mascota: ")

# Convertimos el valor ingresado a entero para poder hacer cálculos
Edad_Perro = int(entrada)

# Definimos una función llamada 'Calcular_Edad' que recibe una edad y la convierte a años perro
def Calcular_Edad(conver_edad): 
    return conver_edad * 7  # Multiplicamos por 7 (1 año humano = 7 años perro)

# Llamamos a la función pasando la edad ingresada y guardamos el resultado en una variable
llamar_funcion = Calcular_Edad(Edad_Perro)

# Mostramos el resultado al usuario
print(f"La edad en años perros de tu mascota es de: {llamar_funcion}")