#+++++++++++++++++++++++++++++++++++++++++++++++++++++++FUNCIONES/METODO++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def saludar(): #Declaramos la funcion
    print("Hola mundo.") #declaramos el funcionamiento de la funcion
saludar() #invocamos esta funcion 




def calcularImpuesto(precio, impuesto = 0.16): 
    print("El producto cuesta", (precio * impuesto) + precio)

calcularImpuesto(500, 0.25)#La llamada a la función debe estar fuera del bloque def

#++++++++++++++++++++++++++++++++++++++++++++METODO parametros arbitrarios || de arreglo+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Definimos una función llamada 'saludarAlumno' que puede recibir muchos nombres
def saludarAlumno(*nombre):
    # El parámetro *nombre convierte los argumentos recibidos en una tupla
    # Por ejemplo, si se pasa ("Gerald", "Anderson", "Jeff"), se guarda como:
    # nombre = ("Gerald", "Anderson", "Jeff")

    # Imprime el segundo nombre (índice 1) de la tupla
    print(nombre[1])

    # Imprime el primer nombre (índice 0) de la tupla
    print(nombre[0])

# Llamamos a la función con tres nombres como argumentos
saludarAlumno("Gerald", "Anderson", "Jeff")

# Resultado en pantalla:
# Anderson
# Gerald

#+++++++++++++++++++++++++++   Metodos con argumentos arbitrarios por llave ++++++++++++++++++++++++++++++++++++++++++++++++++++++


def AgregarInvetario(**articulos):
    print(articulos, type(articulos))
    print(articulos ["jabon"])

    