class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.salud = 50
        self.alimento = 50
        self.higiene = 50
        self.felicidad = 50

    def comer(self):
        self.alimento += 10
        print(f"{self.nombre} ha comido. Alimento actual: {self.alimento}")

    def salud_hp(self):
        self.salud += 10
        print(f"La salud de {self.nombre} ha mejorado: {self.salud} puntos de salud.")

    def banar(self):
        self.higiene += 10
        print(f"{self.nombre} se ha bañado. Higiene actual: {self.higiene}")

    def jugar(self):
        self.felicidad += 10
        print(f"{self.nombre} está feliz. Felicidad actual: {self.felicidad}")

    def estado_actual(self):
        print(f"""
        🌟 Estado de {self.nombre}:
        - Salud: {self.salud}
        - Alimento: {self.alimento}
        - Higiene: {self.higiene}
        - Felicidad: {self.felicidad}
        """)

# Crear el Pokémon
mi_pokemon = Pokemon("Riolu", "Acero")

# Menú
while True:
    print("""
    🧪 MENÚ DE CUIDADO DE POKÉMON 🧪
    1. Alimentar
    2. Mejorar salud
    3. Bañar
    4. Jugar
    5. Ver estado actual
    6. Salir
    """)
    
    try:
        opcion = int(input("Elige una opción (1-6): "))
        print(f"DEBUG: valor ingresado → {opcion} (tipo: {type(opcion)})")

        if opcion == 1:
            mi_pokemon.comer()
        elif opcion == 2:
            mi_pokemon.salud_hp()
        elif opcion == 3:
            mi_pokemon.banar()
        elif opcion == 4:
            mi_pokemon.jugar()
        elif opcion == 5:
            mi_pokemon.estado_actual()
        elif opcion == 6:
            print("👋 Hasta luego, gracias por jugar.")
            break
        else:
            print("❌ Opción inválida.")
    except ValueError:
        print("❌ Ingresa solo números.")