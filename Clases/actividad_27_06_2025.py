class TarjetaDeDebito:
    # Atributos de la clase
    __saldo=0

    # Constructor
    def __init__(self):
        pass

    def abonar(self, monto):
        self.__saldo=self.__saldo+monto
    
    def retirar(self, monto):
        if(monto>self.__saldo):
            print("El monto a retirar es mayor al saldo disponible")
        else:
            self.__saldo-=monto
            print(f"Despues del retiro, su saldo actual es de {self.__saldo}")

    def consultar(self):
        return self.__saldo


tarjeta = TarjetaDeDebito()
print(tarjeta.consultar())

while True:
    input_entrada = int(input("""
Bienvenido al sistema de Tarjeta de Credito:
Por favor ungrese una accion disponible:
    1) Consultar Saldo
    2) Abonar a tarjeta
    3)Realizar un retiro
>>>: """))
    
    
    match input_entrada:
        case 1:
            print(f"Su Saldo es de {tarjeta.consultar()}")
        case 2:
            input_abono = input("Ingrese la cantidad a abonar: >>> ")
            tarjeta.abonar(float(input_abono))
            print("Abono exitoso!")
        case 3:
            input_retiro = input("Ingrese el monto a retirar: >>>")
            tarjeta.retirar(float(input_retiro))
        case _:
            print("Opcion no disponible")