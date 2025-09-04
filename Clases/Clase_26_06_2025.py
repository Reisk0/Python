
#objetos de primera clase

def f_a(f_b): 
    def f_c(): 
        #acciones previas antes de ejecutar la funcion b, la principal
        print("Antes de la funcion de entrada")
        f_b()#Ejecuto mi funcion principal
        print("Despues de la funcion de entrada")
    return f_c

@f_a
def hola(): 
    print("Hola!")

hola()


