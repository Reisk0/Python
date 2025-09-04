# 🐉 CLASE BASE (Padre)
class Criatura:
    # Método constructor que se ejecuta al crear una criatura
    def __init__(self, nombre, tipo, precio):
        self.nombre = nombre        # Nombre de la criatura
        self.tipo = tipo            # Tipo o categoría (ej: fuego, cambiaformas)
        self.precio = precio        # Precio en monedas de oro

    # Método para mostrar la información de una criatura
    def mostrar_info(self):
        print(f"{self.nombre} | Tipo: {self.tipo} | Precio: {self.precio} monedas de oro")


# 🐲 CLASES HIJAS (heredan de Criatura)
class Dragon(Criatura):
    pass  # No agregamos nada nuevo aún, pero hereda todo de Criatura

class Nahual(Criatura):
    pass  # Igual, hereda los atributos y métodos de Criatura


# 🔥 CREACIÓN DE CRIATURAS (Objetos)
dragon = Dragon("Horn", "Fuego", 1500)       # Creamos un dragón con nombre, tipo y precio
nahual = Nahual("Mahichu", "Cambiaformas", 850)  # Creamos un nahual


# 💰 ORO DEL JUGADOR Y SU INVENTARIO
oro = 2000           # El jugador empieza con 2000 monedas de oro
inventario = []      # Lista vacía que guardará las criaturas que el jugador compre


# 📜 MENÚ INTERACTIVO (ciclo que se repite hasta que el jugador elija salir)
while True:
    # Mostramos opciones
    print("\n1. Ver criaturas")
    print("2. Comprar criatura")
    print("3. Ver inventario")
    print("4. Salir")

    # Solicitamos una opción al jugador
    opcion = input("Elige una opción: ")

    # Opción 1: Mostrar criaturas disponibles
    if opcion == "1":
        print("\nCriaturas disponibles:")
        dragon.mostrar_info()     # Usamos el método mostrar_info para cada criatura
        nahual.mostrar_info()

    # Opción 2: Comprar una criatura
    elif opcion == "2":
        print("\n¿Qué quieres comprar?")
        print("1. Horn")
        print("2. Mahichu")
        eleccion = input("Elige 1 o 2: ")

        # Si elige 1 y tiene suficiente oro
        if eleccion == "1" and oro >= dragon.precio:
            inventario.append(dragon)     # Agregamos el dragón al inventario
            oro -= dragon.precio          # Restamos el precio del oro
            print("✅ Has comprado a Horn.")

        # Si elige 2 y tiene suficiente oro
        elif eleccion == "2" and oro >= nahual.precio:
            inventario.append(nahual)     # Agregamos el nahual al inventario
            oro -= nahual.precio          # Restamos el oro
            print("✅ Has comprado a Mahichu.")

        # Si no tiene suficiente oro
        else:
            print("❌ No tienes suficiente oro.")

    # Opción 3: Ver inventario
    elif opcion == "3":
        print("\n📦 Tu inventario:")
        if not inventario:                # Si está vacío
            print("Vacío.")
        else:
            for criatura in inventario:   # Recorremos y mostramos cada criatura
                criatura.mostrar_info()
        print(f"Oro restante: {oro}")

    # Opción 4: Salir
    elif opcion == "4":
        print("¡Gracias por jugar! 🐉")
        break   # Salimos del ciclo

    # Opción inválida
    else:
        print("❌ Opción inválida.")