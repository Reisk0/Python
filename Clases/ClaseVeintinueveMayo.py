
texto1= ""
texto2= ''
texto2 = "\n"

# \n enter o salto de linea
# \t tabuladro tabs
texto= """
\tlinea uno
\tlinea dos
\tlinea tres
"""
texto = "linea uno \n linea dos"
texto_nombre = "Diego Sait" \
" Grande Camacho"

print(texto_nombre)
texto_largo = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

# un string se puede tratar como una lista de caracteres
for letra in texto_largo:
    print(letra)
print(texto_largo[0])


# slicing (rebanado o segementacion)
print(texto_largo[4:20])
#          0  1  2  3  4 5  6
edades = [18,18,34,43,23,5,10]

# [indice donde vamos a empezar: indice del final (sin contarlo):paso]
print(edades[2:6])
print(texto_largo[6:11])

# le decimos donde termina pero no donde empieza
print(texto_largo[:25:2])

# le decimos donde empieza pero no donde termina
print(texto_largo[2::5])

# no le decimos ni donde empieza ni donde termina, pero si que vaya de 5 en  5
print(texto_largo[::-1])

print(texto_largo[4:-4])


#### FORMATOS

nombre= "Juan Perez"
edad = 38 

saludo = "Hola "+nombre+"!, tienes "+str(edad)+" años"
saludo = "Hola %s!, tienes %s años" % (edad, nombre)
saludo = "Hola {}!, tienes {} años".format(nombre, edad)
saludo = f"Hola {nombre}!, tienes {edad} años."

from string import Template
saludo = Template("Hola $nombre!, tienes $edad años. Estado civil: $estado").substitute(edad=edad, nombre=nombre, estado="soltero")

print(saludo)

# Primera meyuscula de la oracion
print(texto.capitalize())
#Todo min
print(texto_largo.lower())
# Todo mayusculas
print(texto_largo.upper())
# Quitar espacios en blanco derecha o izquierda
print("   Hola grupo".lstrip())
print("Hola     ".rstrip())
#invierte mayus/minus
print("assDFRDs HolA".swapcase())
# Mayuscula en la primera letra de cada palabra
print(texto_largo.title())

# Muestra una cadena grande de n cantida, toma nuestros string, 
# lo centra y llena 
# los espacios vacios con un simbolo elegido
print(texto_largo.center(75, "*"))
print(texto_largo.replace("e","E"))
print("8556234".zfill(15).replace("0","N").lower())

alfa = "12345345"
print(alfa.isalnum())
print(alfa.isnumeric())
print(alfa.isalpha())
print(alfa.isdecimal())
print(alfa.isdigit())
print(alfa.isspace())