# 🌟 CLASE BASE: POKEMON
class Pokemon: 

    # Constructor que define nombre, tipo, poder de combate (CP) y puntos de vida (HP)
    def __init__(self, nombre, tipo, CP, HP):
        self.nombre = nombre                  # Nombre del Pokémon
        self.tipo = tipo                      # Tipo elemental (fuego, agua, fantasma, etc.)
        self.CP = int(CP)                     # CP: Poder de combate (daño que hace)
        self.HP = int(HP)                     # HP: Puntos de salud

    # Método para mostrar la información del Pokémon
    def Pok_Info(self): 
        print(f"Nombre: {self.nombre} || Tipo: {self.tipo} || CP: {self.CP} || HP: {self.HP}")

    # Método para atacar a otro Pokémon
    def atacar(self, objetivo):
        objetivo.HP -= self.CP                # Resta los puntos de CP al HP del objetivo
        if objetivo.HP < 0:                   # Si el HP baja de 0, lo fijamos en 0
            objetivo.HP = 0
        print(f"\n⚔️ {self.nombre} ataca a {objetivo.nombre} y le quita {self.CP} puntos de HP.")
        print(f"❤️ {objetivo.nombre} tiene ahora {objetivo.HP} HP.\n")


# 🟦 CLASE HIJA: RIOLU (tiene habilidad especial Aura)
class Riolu(Pokemon): 
    def __init__(self, nombre, tipo, CP, HP, Aura):
        super().__init__(nombre, tipo, CP, HP)    # Heredamos atributos de la clase base
        self.Aura = int(Aura)                     # Aura: poder especial extra

# Función que activa el boost de Aura cuando Riolu está en peligro
def Aur(riolu):
    riolu.CP += riolu.Aura                        # Aumentamos el CP con Aura
    print("✨ Riolu se siente acorralado. ¡Su aura se intensifica!")
    print(f"⚡ Su poder (CP) ha aumentado a {riolu.CP}.\n")


# 🟪 CLASE HIJA: ZORUA (tiene habilidad especial Trickster)
class Zorua(Pokemon):
    def __init__(self, nombre, tipo, CP, HP, Trickster):
        super().__init__(nombre, tipo, CP, HP)    # Heredamos atributos
        self.Trickster = int(Trickster)           # Trickster: habilidad curativa

# Función que activa el truco curativo de Zorua
def Trick(zorua):
    zorua.HP += zorua.Trickster                  # Aumentamos los puntos de HP
    print("🎩 Zorua recurre a sus trucos para curarse.")
    print(f"💚 Su HP aumenta a {zorua.HP}.\n")


# 🧪 INSTANCIAS DE LOS POKEMON
riolu = Riolu("Riolu", "Acero", 20, 80, 15)       # Nombre, tipo, CP, HP, Aura
zorua = Zorua("Zorua", "Fantasma", 15, 85, 30)    # Nombre, tipo, CP, HP, Trickster


# 🔍 MOSTRAR ESTADÍSTICAS INICIALES
print("🌟 ESTADÍSTICAS INICIALES 🌟")
riolu.Pok_Info()
zorua.Pok_Info()

# 🧠 APLICAR HABILIDADES PASIVAS ANTES DE COMENZAR
Trick(zorua)   # Zorua se cura al inicio
Aur(riolu)     # Riolu recibe boost al inicio


# 🕹️ SISTEMA DE COMBATE POR TURNOS
turno = 1  # Comenzamos desde el turno 1

while True: 
    # Solicita al usuario que elija un Pokémon o termine el combate
    Entrada = input("\nSelecciona tu Pokémon para el combate ('Riolu', 'Zorua') o escribe 'Salir' para terminar: ").upper()

    # Si el texto no es válido, vuelve a pedir
    if Entrada not in ["RIOLU", "ZORUA", "SALIR"]:
        print("⚠️ Opción inválida. Elige entre 'Riolu', 'Zorua' o 'Salir'.")
        continue

    # Muestra el número de turno actual
    print(f"\n🔁 Turno número {turno}")

    try: 
        # Si el usuario elige a Riolu, ataca a Zorua
        if Entrada == "RIOLU": 
            riolu.atacar(zorua)
            turno += 1

        # Si elige a Zorua, ataca a Riolu
        elif Entrada == "ZORUA": 
            zorua.atacar(riolu)
            turno += 1

        # Si escribe "Salir", termina el bucle
        elif Entrada == "SALIR":
            print("👋 Combate terminado por el jugador.")
            break   

        # Revisa si Riolu ha perdido toda su vida
        if riolu.HP <= 0:
            print("💥 Riolu ha caído. El combate termina.")
            break

        # Revisa si Zorua ha perdido toda su vida
        if zorua.HP <= 0:
            print("💥 Zorua ha caído. El combate termina.")
            break

        # Habilidad especial de Riolu si está en riesgo y aún no ha recibido boost extra
        if riolu.HP <= 35 and riolu.CP <= 30:
            Aur(riolu)

        # Habilidad especial de Zorua si está en riesgo y aún puede curarse
        if zorua.HP <= 35 and zorua.HP < 100:
            Trick(zorua)

    except ValueError: 
        print("⚠️ Error inesperado. Intenta de nuevo.")