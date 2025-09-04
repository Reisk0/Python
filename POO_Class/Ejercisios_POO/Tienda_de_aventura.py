"""
 📌 Instrucciones:
	1.	Define la clase y sus atributos.
	2.	Crea al menos 3 instancias con diferentes valores.
	3.	Llama a los métodos para simular una compra y una reposición.
	4.	Usa mostrar_info() después de cada cambio para ver el estado.
"""

class Tienda: 
    def __init__(self, nombre, categoria, precio, disponibilidad):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = int(precio)
        self.disponibilidad = bool(disponibilidad)

    def mostrar_info(self): 
        print(f"Producto: {self.nombre}|| Categoria: {self.categoria} || Precio: {self.precio} || Disponibilidad {self.disponibilidad}")

    def comprar_producto(self): 
        if self.disponibilidad == True: 
            self.disponibilidad = False
            print(f"✅ El producto '{self.nombre}' fue comprado. Disponibilidad: {self.disponibilidad}")
        else:
            print(f"⚠️ El producto '{self.nombre}' ya fue vendido o no está disponible.")

class sword(Tienda): 
    def __init__(self, nombre, categoria, precio, disponibilidad):
        super().__init__(nombre, categoria, precio, disponibilidad)

Espada = sword("Espada de Hierro", "Arma", 1500, True)

Espada.mostrar_info()

Mochila_de_aventurero = []

while True: 
    entrada = input("Bienvenido a la tienda:\n1.- Inventario\n2.- Comprar\n3.- Vender\n4.- Mochila\n> 5.- Salir\n> ")

    try: 
        if entrada.lower() == "inventario": 
            Espada.mostrar_info()
            continue
        elif entrada.lower() == "salir": 
            break
        elif entrada.lower() == "comprar": 
            Espada.comprar_producto()
            Mochila_de_aventurero.append(Espada)
            continue
        elif entrada.lower() == "mochila":
            print("🎒 Mochila del aventurero:")
            for item in Mochila_de_aventurero:
                print(f"- {item.nombre}")
    except ValueError: 
        print("Opcion no valida, elige una opcion del menu")