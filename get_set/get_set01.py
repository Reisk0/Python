
# Propiedades - son variables que son atributos de clase que son accesibles mediante getters y seters

#getter - es para obtener lo que tienen la variable
#setter _ es para meterle informacion a la variable

class Carrito:
    __cantidad_de_articulos = 0

    def __init__(self):
        pass
    
    #getter - por que esta mostrando su valor interior
    #formula: @property
    #def nombre_publico(self): 
    # return sekf|,
    @property 
    def cantidad_de_articulos(self): 
        return self.cantidad_de_articulos
    
    @cantidad_de_articulos.setter
    def cantidad_de_articulos(self, value): 
        self.__cantidad_de_articulos=value 

        carrito = Carrito()
        print(carrito.cantidad_de_articulos)
        carrito.cantidad_de_articulos=12 
        print(carrito.cantidad_de_articulos)