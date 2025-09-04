
#ESTRUCTURA DE DATOS. 
#---------------------------------------------------LISTAS---------------------------------------------------------------------
#posicion    0         1        2       3          4
my_list = ["Alex", "Alberto", "Saul", "Raul", "Valentina"] #Esto es una lista
print(my_list[2]) #imprimir la posicion 2 = "Saul"

#agregar elemento al lugar de la lista
my_list.append("Diego") 
print(my_list[5]) #imprimir la posicion 5 "Diego"

#Agregar elemento en la posicion que queramos 
my_list.insert(2, "Jesus") #agregaremos a jesus en la posicion 2
print(my_list)

#fusionar listas
my_list_dos= ["Armando", "Francisco"]
my_list.extend(my_list_dos) #ahora se agrega la lista dos despues de la primera
print(f"fusionar listas {my_list}")

#Remover elemento pero tendras que ingresar el elemento a remover directamente
my_list.remove("Saul")
print(f"Remover elemento 1 {my_list}")
print(my_list)

my_list_numero = [1, 2, 51, 20, 0]
#ordenar lista
my_list_numero.sort()
print(f"ordenar lista: {my_list_numero}")

#revertir orden de lista
my_list_numero.reverse()
print(f"reverti lista: {my_list_numero}")

#limpia la lista
my_list_numero.clear()
print ((f"limpiar {my_list_numero}"))


#Eliminar ultimo elemento pop 
my_list_numeroA = [1, 2, 3, 4, 5]
eliminado = my_list_numeroA.pop()
print(f"Elemento eliminado: {eliminado}")
print(f"Lista actualizada: {my_list_numeroA}")

#falta len


#--------------------------------------------------TUPLAS-------------------------------------------------------------------------------

my_tupla = (1,2,3,4,5,6,7,8,9) 
my_tupla_nombre = ("Alex", "Alberto", "Saul", "Raul", "Valentina")

print(my_tupla.count(5)) #cantidad que se repite un elemento
print(my_tupla_nombre.count("Alberto")) #cantidad que se repite el nombre, debe estar tal cual (case sensitive)

print(f"posicion del numero siete {my_tupla.index(7)}") #imprimir elemento 7 el cual es 6

print(my_tupla[-5]) #imprimira la lista del derecha izquierda si ingresamos numeros negativos.


#-------------------------------------------Diccionario-------------------------------------------------------------

my_diccionario = {
    "Nombre": "Saul Flores", 
    "Edad": 27, 
    "Soltero": True,
    "Carrera": "Desarrollador de software"
    }

my_diccionario_dos = {
    "Nombre": "Saul Flores", 
    "Edad": 27, 
    "Carrera": "Desarrollador de software"
    }
print(my_diccionario["Nombre"])
print(my_diccionario_dos.get("Soltero", "NO INFO")) #cuando no se encuentra un tipo de dato
print(len(my_diccionario)) #cuantos elementos hay dentro del diccionario
print(my_diccionario.keys()) #se guardan las palabras clave del diccinario para identidicarlas con mas facilidad

llaves = my_diccionario.keys()
for propiedad in llaves: 
    print(my_diccionario[propiedad])


# Ejersico de la clase
tabla = [
        {"nombre": "castian", "valor": 10, "posicion": 1}, 
        {"nombre": "edrian", "valor": 15, "posicion": 2},
        {"nombre": "Elizabeth", "valor": 3, "posicion": 3},
        {"nombre": "Darien", "valor": 1, "posicion": 4},
        {"nombre": "Mael", "valor": 19, "posicion": 5},
    ]

for i in tabla:
    print(i["nombre"], i["valor"]* i["posicion"])