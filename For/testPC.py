#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++len()++++++++++++++++++++++++++++++++++++++++++++++++++++ 

#contador de frases en mayuscula 
contador = 0
lista_palabras = []
entrada = input("Ingresa una frase, contaremos cuantas palabras tiene esta oracion: ").lower()

frase = entrada.split()
for ciclo in frase: 
      contador += 1
      lista_palabras.append(ciclo)
print(f"la cantidad de palabras en la oracion es de {contador} y estas son {lista_palabras}")


frase = input("Ingresa una frase, contaremos cuántas palabras tiene: ").lower().split()
print(f"La cantidad de palabras es {len(frase)} y estas son: {frase}") #len() te dice cuántos elementos hay en algo.


#cuenta cuantas palabras existen en la frase e imprimelas en mayusculas. 
frase = input("Ingresa una frase: ")
palabras = frase.split()
print(f"La frase tiene {len(palabras)} palabras:")

for palabra in palabras:
    print(palabra.upper())