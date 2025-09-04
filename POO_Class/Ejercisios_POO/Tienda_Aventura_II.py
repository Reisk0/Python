class Personaje: 
    def __init__(self, nombre, titulo, CP, HP, Habilidad_Especial):
        self.nombre = nombre
        self.titulo = titulo
        self.CP = int(CP)
        self.HP = int(HP)
        self.Habilidad_Especial = Habilidad_Especial 
        self.equipo = []                      # Lista de objetos equipados
        self.Creditos_Recompensa = 3000       # Créditos iniciales del personaje

    def Personaje_info(self): 
        # Muestra toda la información del personaje
        print(f"\n👤 {self.nombre} - '{self.titulo}'")
        print(f"CP: {self.CP} | HP: {self.HP} | Habilidad Especial: {self.Habilidad_Especial} | Créditos: {self.Creditos_Recompensa}")

    
    def equipar_item(self, item):
    # Este método permite equipar un ítem al personaje, si el ítem está disponible.
        if item.disponibilidad:
        # Verifica si el ítem está disponible (True).
        # Solo se puede equipar si no ha sido usado o comprado antes.
            self.equipo.append(item)
        # Si el ítem está disponible, se agrega (append) al inventario personal del personaje (su lista 'equipo').
            item.disponibilidad = False
        # Una vez equipado, el ítem ya no está disponible para otros usos, así que se marca como no disponible.
            print(f"✅ {item.nombre} ha sido equipado por {self.nombre}.")
        # Se muestra un mensaje informando que el ítem fue equipado exitosamente.
        else:
        # Si el ítem NO está disponible (ya fue usado o comprado), se ejecuta este bloque.
            print(f"⚠️ {item.nombre} no está disponible.")
        # Se muestra una advertencia diciendo que ese ítem no se puede equipar.

    def comprar_item(self, item): 
        if self.Creditos_Recompensa >= item.precio: 
            self.Creditos_Recompensa -= item.precio
            self.equipo.append(item)
            item.disponibilidad = False
            
            # Aumentamos los puntos básicos del ítem
            self.CP += item.Puntos_de_aumento

            # Si el ítem es una Sword, aplicamos el Legado de Héroe
            if isinstance(item, Sword):
                self.CP += item.Legado_de_Heroe
                print(f"✨ Legado de héroe activado: +{item.Legado_de_Heroe} CP extra.")

            print(f"✅ {item.nombre} comprado y equipado. Créditos restantes: {self.Creditos_Recompensa}")
            print(f"🛡️ CP aumentado a {self.CP}")
            print("🎒 Objetos equipados:")
            for obj in self.equipo:
                print(f"- {obj.nombre}")
        else:
            print("❌ Créditos insuficientes, necesitas conseguir más trabajos.")

# Clase base para los ítems
class Item: 
    def __init__(self, nombre, categoria, precio, disponibilidad, Puntos_de_aumento):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = int(precio)
        self.disponibilidad = bool(disponibilidad)
        self.Puntos_de_aumento = int(Puntos_de_aumento)

    def item_info(self): 
        # Muestra la información del ítem
        estado = "Disponible" if self.disponibilidad else "No disponible"
        print(f"Item: {self.nombre} || Tipo: {self.categoria} || Precio: {self.precio} || Estado: {estado}")

# Subclase de arma especial
class Sword(Item): 
    def __init__(self, nombre, categoria, precio, disponibilidad,Puntos_de_aumento, Legado_de_Heroe):
        super().__init__(nombre, categoria, precio, disponibilidad, Puntos_de_aumento)
        self.Legado_de_Heroe = int(Legado_de_Heroe)

# Instancias de ítems y personaje
black_sword = Sword("Buster Sword", "Espada Pesada", 1500, True,1000, 500)
daga = Item("Daga_Acero_negro", "Arma", 800, True, 600)
anillo = Item("Anillo_de_Plata", "Regeneración", 250, True, 500)
bufanda = Item("Bufanda_Negra", "Defensa", 800, True, 200)
sniper = Item("Sniper_balas_explosivas", "Arma de fuego", 1500, True, 800)

# Instancia del personaje
Cloud = Personaje("Cloud_Strife", "Black_Knight", 5000, 10000, "Buster_Strike")

# Inventario general disponible
inventario_disponible = [black_sword, daga, anillo, bufanda, sniper]

# Función para mostrar inventario
def mostrar_inventario(lista_inventario):
    print("\n=== Inventario disponible ===")
    for item in lista_inventario:
        item.item_info()

# Bucle principal del menú
while True: 
    entrada = input("\nSelecciona un comando: \n1.- Ver personaje \n2.- Ver Inventario \n3.- Comprar objeto \n4.- Terminar\nComando: ")

    try: 
        if entrada == "1":
            # Mostrar personaje
            Cloud.Personaje_info()

        elif entrada == "2":
            # Mostrar el inventario
            mostrar_inventario(inventario_disponible)

        elif entrada == "3":
            # Mostrar ítems numerados para que el jugador elija
            print("\n¿Qué objeto deseas comprar?")
            for i, item in enumerate(inventario_disponible):
                print(f"{i + 1}. {item.nombre} - Precio: {item.precio} - Estado: {'Disponible' if item.disponibilidad else 'No disponible'}")
                if isinstance(item, Sword):
                    print("⚔️ Legado de héroe activo: +500 CP adicionales, acabalos!!! ⚔️.")

            opcion = input("Ingresa el número del objeto: ")
            if opcion.isdigit():                             # Verificamos que la entrada sea un número
                indice = int(opcion) - 1                     # Convertimos a índice de lista (comienza en 0)
                if 0 <= indice < len(inventario_disponible):
                    Cloud.comprar_item(inventario_disponible[indice])
                else:
                    print("❌ Número fuera de rango.")
            else:
                print("❌ Entrada inválida. Debes escribir un número.")

        elif entrada == "4":
            # Finalizar el programa
            print("✅ Equipo terminado. ¡Listo para el viaje!")
            break

        else:
            print("❌ Comando no reconocido. Intenta de nuevo.")
            
    except ValueError: 
        print("❌ Ocurrió un error. Intenta nuevamente.")