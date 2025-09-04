
#___________________________________Modificacion de las Strings y Listas________________________________________________________________

textoLargo = "esta es una prueba para poder manipular las cadenas de texto"

print(textoLargo[1]) # imprime la letra en la posicion 1

print(textoLargo[4:20])


edades = [10,18,94,50,6,27] #[indice donde vamos a empezar: indice del final (cin contarlo): paso]
print(edades[2:4]) #trame el 94 y 50 dependiendo de su posicion, podemos extraer fraccion de una cadena de texto. 
print(edades[2::3])# esto imprimira fracciones de texto de tres en tres por ejemplo empeiza en el punto dos y ve de tres en tres
print(edades[:10:3])# aqui le decimos donde termina pero no donde empieza pero va a ir de tres en tres

# empieza, termina, saltos(de 3 en 3)
print(edades[2:10:3])

print(textoLargo[::-1]) #esto invierte la cadena de texto o numeros

texto_Encriptado1 = "h4HBarodatupmocb5Eb" 
texto_Encriptado2 = "DTALamargorpeKxu" 
texto_Encriptado3 = "kv3qsenoicnufSrC2" 
texto_Encriptado4 = "fPfJnohtypeqRO" 
texto_Encriptado5 = "f4SselbatucejeQZuJ" 

print(texto_Encriptado1[14:3:-1])
print(texto_Encriptado2[11:3:-1])
print(texto_Encriptado3[12:3:-1])
print(texto_Encriptado4[9:3:-1])
print(texto_Encriptado5[13:3:-1])
# h  4  H  B  a  r  o  d  a  t  u  p  m  o  c  b  5  E  b
# 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18
"""
	•	Inicio en índice 14 → 'c'
	•	Fin en índice 3 → hasta antes de 'B'
	•	Avanza de -1 en -1 (de derecha a izquierda)
"""


#-------------------------------------------------------FORMATEO---------------------------------------------------------------------------

nombre = "Anderson"
edad = 94

saludo = "hola %s!, tienes %s años" % (nombre, edad)
saludo = "hola %s, tienes %s años" % (nombre, edad)
saludo = "hola {}, tienes {} años".format(nombre, edad)
print(saludo)

#Primera Mayuscula
print(textoLargo.capitalize())
#Todas minusculas
print(textoLargo.lower())
#Todas mayusculas
print(textoLargo.upper())
#quita los espacios en blanco desde la izquierda
print("       Prueba de texto".lstrip())
#quita los espacios en blanco desde la izquierda
print("Prueba de texto     ".lstrip())
#Invierte la ,¿mayuscular y minusculas
print("uasjasBIHNOIbhj".swapcase())
#Pone una mayuscula en la primera letra de cada palabra
print(textoLargo.title())

#muestra una cadena grande de n cantidad y llena los espacios vacios con un simbolo elegido
print(textoLargo.center(100, "=")) 

print(textoLargo)
