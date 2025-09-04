PalabrasFiltradas = []

for palabras in range(5): 
    entrada = input("Ingresa palabras que NO empiecen con la letra a: ").lower()

    if entrada.startswith("a"):
        print("La palabra comienza con 'a': trata de nuevo.")
    else:
        PalabrasFiltradas.append(entrada)
        print(f"Palabras filtradas: {PalabrasFiltradas}")