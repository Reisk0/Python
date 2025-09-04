
class Estudiante():
    materias = ["POO", "Progrmacion funcionnal", "Programacion Web"]

    def __init__(self, nombre, edad, matricula): #Constructor: es el metodo o funcion que se ejecuta automaticamente cuando instanciamos la clase 
        self.nombre = nombre            #Self es un parametro obligatorio, es el que da el contexto
        self.edad = edad
        self.matricula = matricula

    def hacer_tarea(self):
        print(f"{self.nombre} esta haciendo tarea")

    def comer(self, comida): 
        print(f"{self.nombre} esta comiendo {comida}")

Saul = Estudiante("Saul", 27, "Sa27")
                  #Nombre Edad Matricula
aldalberto = Estudiante("Adalberto", 45, "Adal45")

print(Saul.nombre, aldalberto.nombre)
print(Saul.matricula, aldalberto.matricula)
Saul.hacer_tarea()
aldalberto.comer("Enchiladas")



#Caracterisitcas de la programacion orientada a objetos. 

"""
1.-Encapsulamiento
2.-Herencia
3.-Polimorfismo
4.-Abastraccion
"""

#Encapsulamiento - Ocultar es estado interno de los objetos
class CuentaBancaria: 
    def __init__(self, saldo):
        saldo._saldo = saldo

    #Nos permite tener un tunel o ingreso controlado para dejarnos ver lo que queremos y lo que no queremos

    def depositar(self, cantidad): 
        self._saldo = cantidad

    def obtener_saldo(self): 
        return self._saldo
    
cuenta_de_Diego = CuentaBancaria(100)
print("Saldo de Diego", cuenta_de_Diego.obtener_saldo())
cuenta_de_Diego.depositar(5000)
print("Saldo de Diego", cuenta_de_Diego.obtener_saldo())


#Herencia 
class Animal: 
    def hablar(self):
        print("Hacer sonido")



