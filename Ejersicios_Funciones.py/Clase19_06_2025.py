#Programacion orientada a objetos
class Animal(): 
    color = "Negro"
    patas = "cuatro"
    ojos = "dos"
    genero = "F"

    def comer(self): 
        print("esta comiendo carne")

    def dormir(self): 
        print("duerme de dia")
#otra clase
class Estudiante: 
        nombre = ""
        edad = 10
        materias = []
        def hacer_tareas(self): #estamos definiendo las acciones que puede relizar NO las caracteristicas 
                    print("Progra todos los dias")

        def salir_a_comer(self):
                    print("Fue a comer")


#Instancia, una "creacion" a partir de una plantilla (clase). 
# Un objeto es la instancia de una clase
#Instanciacion
#La clase es ese modelo ideal y la instancia es ese objeto en concreto, esa materializacion de ese modelo ideal
    

    #class Estudiante es la clase
    #Estudiante() es la intancia, es el llamado, la invocacion
    #saul es el objetom es esa intancia cocreta o materializada
saul = Estudiante()
breno = Estudiante()
alejandro = Estudiante()

print(saul.edad)
saul.hacer_tareas()
saul.salir_a_comer()
