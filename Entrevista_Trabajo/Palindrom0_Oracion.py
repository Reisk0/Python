"""
🧩 Reto: Palíndromos en una frase

Escribe un programa en Python que:
	1.	Pida al usuario una frase.
	2.	Separe la frase en palabras.
	3.	Encuentre todas las palabras que sean palíndromos (que se leen igual al derecho y al revés).
	4.	Las muestre en pantalla junto con cuántas encontró.
"""

frase = input("Ingresa una oracion: ").lower()

palindromos = 0
lista_pal = []

for palabra in frase.split():
    if palabra == palabra[::-1]: 
        palindromos += 1
        lista_pal.append(palabra)
        print(f"La palabra '{palabra}' es un palindromo")

print(f"Numero de palindromos encontrados: {palindromos}")
print("Lista:", ", ".join(lista_pal))