
while True: 
    input_nombre = input("Escribe tu nombre: ")
    input_apellido = input("Escribe tu apellido: ")
    input_calificacion = input("Escribe tu calificacion: ")

    string_output = f"{input_nombre}, {input_apellido}, {input_calificacion}/n"
    print(string_output)
    
    with open(file = "persona-txt", mode = "a", encoding= "utf8") as file:
        file.write(string_output)
