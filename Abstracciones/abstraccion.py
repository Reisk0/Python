#Abstraccion - ocultar la complejidad para el que cosume la class con una interfaz sencilla. 

class lavadora: 
    #llegar agua
    #echarle savitel
    #prender
    #drenar
    #secar

    def lavar(self):
        self.__llenar()
        self.__suavizante()

    def __llenar(self): 
        print("Se esta llenando de agua")

    def __suavizante(self): 
        print("Se esta agregando el suavizante")   


mabe023 = lavadora()
mabe023.lavar()
