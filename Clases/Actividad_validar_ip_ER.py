# importamos la libreria
import re

# creamos una expresion regular
# regla 1: el or se lee de dereche a izquierda
# regla 2: a veces es necesario identificar el tipo de dato
# un \d
regexp = r"^([1-9]\d{0,2}|[1-9])\.(\d{1,3})\.(\d{1,3})\.([0-9]{1,3})$"
regexp_alejandro = r"^([1-9][0-9]{0,2}|[1-9])\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$"

# creamos un ciclo para estarlo probando
while True:
    print("Escribe una direccion ip valida:")
    input_ip = input(">> ")

    res = re.match(regexp_alejandro, input_ip)

    if res is not None:
        print(f"La ip {input_ip} es valida")
    else:
        print(f"La ip {input_ip} no es valida")