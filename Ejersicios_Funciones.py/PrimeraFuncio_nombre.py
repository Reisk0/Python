
# Solicitamos al usuario que escriba su nombre y lo guardamos en la variable 'nombre'
nombre = input("Escribe tu nombre: ")

# Definimos una función llamada 'saludar' que recibe un parámetro llamado 'usuario'
def saludar(usuario): 
    # La función simplemente devuelve el valor del parámetro que se le pasó (el nombre)
    return usuario

# Llamamos a la función 'saludar' pasando el nombre ingresado por el usuario
# y guardamos el valor que regresa en la variable 'resultado'
resultado = saludar(nombre)

# Mostramos un mensaje en consola usando la variable 'resultado' para personalizarlo
print(f"Hola {resultado} Bienvenido/a al sistema.")