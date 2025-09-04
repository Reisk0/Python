# Definimos una clase llamada 'Pokemon' (por convención se usa mayúscula inicial)
class Pokemon:

    # Este es el método constructor. Se ejecuta automáticamente al crear un objeto.
    def __init__(self, nombre, tipo):
        # 'self.nombre' guarda el valor del parámetro 'nombre' como un atributo del objeto
        self.nombre = nombre
        # 'self.tipo' guarda el tipo del Pokémon como atributo del objeto
        self.tipo = tipo

    # Este es un método de la clase llamado 'atacar'
    # 'self' representa al objeto actual que llama este método
    def atacar(self):
        # Imprime un mensaje con el nombre y tipo del Pokémon
        print(f"{self.nombre} ataca con un movimiento tipo {self.tipo}!")

# Aquí creamos una instancia (objeto) de la clase Pokemon llamada 'riolu'
# Le pasamos el nombre "Riolu" y el tipo "Acero"
riolu = Pokemon("Riolu", "Acero") #🫀ESTE ES EL OBJETO

# Imprimimos el atributo 'nombre' del objeto 'riolu'
print(riolu.nombre)

# Imprimimos el atributo 'tipo' del objeto 'riolu'
print(riolu.tipo)

# Llamamos al método 'atacar' del objeto 'riolu'
riolu.atacar()