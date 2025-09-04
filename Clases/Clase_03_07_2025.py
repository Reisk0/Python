#Excepciones
#Tipos de errores: 
#Errores de sintxis 
#Errores de ejecucion

"""
try: 
    algo
except: 
que vamos a hacer con el error
"""

dict = {"nombre":"juan", "estado_civil": "soltero"}

while True: 
    try:
        input_numero = int(input("Escribe un numero para dividir: "))
        division = 450 / input_numero #esta prohibido dividir entre cero o letras
        print(division)
        print(dict["edad"]) #aqui no podemos pedir el valor de una llave que no existe
    except: 
        print("Ocurrio un error!")


# Existen tres tipos de excepciones: Especificas, del SO, advertencias
# Especificas: ZerodivisionError: division by zero
