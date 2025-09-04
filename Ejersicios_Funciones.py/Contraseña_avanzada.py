"""
✅ Requisitos de la contraseña:
	1.	Debe tener al menos 8 caracteres.
	2.	Debe contener al menos una letra mayúscula.
	3.	Debe contener al menos una letra minúscula.
	4.	Debe contener al menos un número.
	5.	Debe contener al menos un carácter especial (!@#$%^&*()_+{}[] etc.)
"""

simbolos = "!@#$%^&*()_+-={}[]:;<>?."

while True: 
    entrada = input("Ingresa una contraseña: ")

    inicia_mayus = False
    tiene_minus = False
    tiene_num = False
    caracter_esp = False

    for letra in entrada: 
        if letra.islower(): 
            tiene_minus = True
        if letra.isdigit(): 
            tiene_num = True
    
    # Verificar si la primera letra es mayúscula
    if entrada[0].isupper():
        inicia_mayus = True

    # Verificar si tiene al menos un símbolo especial
    if any(caracter in simbolos for caracter in entrada):
        caracter_esp = True

   