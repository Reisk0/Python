entrada = input("Ingresa varias cantidades separadas por comas (ej. 5,2,-3,8): ")
lista = entrada.split(",") # Separa los elementos por coma

Lista_numeros = [] # Lista donde guardaremos los números convertidos a enteros

try:
    for elemento in lista:
        elemento = elemento.strip()  # Elimina espacios extra
        if elemento == "":  # Verifica que no esté vacío
            raise ValueError("Se encontró un valor vacío.")
        numero = int(elemento)
        Lista_numeros.append(numero)

    print(f"El número de datos es: {len(Lista_numeros)}.")
    print(f"La suma de los datos es: {sum(Lista_numeros)}.")
    print(f"Lista ordenada de menor a mayor: {sorted(Lista_numeros)}.")

except ValueError:
    print("Dato inválido. Asegúrate de ingresar solo números enteros separados por comas.")