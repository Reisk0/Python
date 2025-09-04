#COMO IDENTIFICAR EL TIPO DE ERROR

dict = {"nombre":"juan", "estado_civil": "soltero"}

while True: 
    try:
        input_numero = int(input("Escribe un numero para dividir: "))
        division = 450 / input_numero #esta prohibido dividir entre cero o letras
        print(division)
        print(dict["edad"]) #aqui no podemos pedir el valor de una llave que no existe
    except Exception as miError: #asi podremos identificar el error y saber que hacer con el
        print(f"Ocurrio un error! - {miError} - {type(miError)}")