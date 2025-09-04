#EXPRESIONES REGULARES (REGEX)
import re
#search
res = re.search("Lola", "Hola Lola")
print(res)
if res is not None: 
    print(res [0], f"Inicia en {res.start()} y termina en {res.end()}")
else: 
    print("No lo encontramos")

#match, busca empezando la cadena de texto
res2 = re.match("lola", "hola lola")
if res2 is not None: 
    print(res2 [0], f"Inicia en {res.start()} y termina en {res.end()}")