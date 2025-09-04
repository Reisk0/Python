import random

# Clase base
class Personaje: 
    def __init__(self, nombre, raza, fuerza, salud):
        self.nombre = nombre
        self.raza = raza
        self.fuerza = int(fuerza)
        self.salud = salud

    def mostrar_personaje(self): 
        print(f"🎭 Personaje: {self.nombre} | Raza: {self.raza} | Fuerza: {self.fuerza} | Salud: {self.salud}")

    def atacar(self, objetivo):
        if self.salud <= 0:
            print(f"⚠️ {self.nombre} está fuera de combate y no puede atacar.")
            return
        print(f"{self.nombre} ataca a {objetivo.nombre} y lo ha debilitado.")
        objetivo.salud -= self.fuerza
        if objetivo.salud < 0:
            objetivo.salud = 0
        print(f"La salud de {objetivo.nombre} ahora es: {objetivo.salud}")

    def esta_vivo(self):
        return self.salud > 0


# Clases hijas
class Devil_Hunter(Personaje): pass
class Vampire_Noble(Personaje): pass
class Black_Knight(Personaje): pass
class White_Rabbit(Personaje): pass
class Abyss_Monster(Personaje): 
    def atacar_jugador(self, objetivo):
        if self.salud <= 0:
            print("☠️ El Abismo fue derrotado. No puede contraatacar.")
            return
        print(f"\n💀 Kariu contraataca a {objetivo.nombre}...")
        objetivo.salud -= self.fuerza
        if objetivo.salud < 0:
            objetivo.salud = 0
        print(f"🔥 La salud de {objetivo.nombre} ahora es: {objetivo.salud}")

# Instancias de personajes
cazador = Devil_Hunter("Dante", "Cazador de Demonios", 1500, 5000)
vampiro = Vampire_Noble("Alucard", "Vampiro Noble", 980, 5000)
caballero = Black_Knight("Igris", "Caballero Negro", 1800, 5000)
conejo = White_Rabbit("Bell", "White Rabbit", 850, 5000)
abismo = Abyss_Monster("Kariu", "Monstruo del Abismo", 2500, 15000)

# Lista de personajes vivos (para que el abismo elija a uno)
heroes = [cazador, vampiro, caballero, conejo]

# Contador de turnos
turno = 1

# Menú interactivo
while True:
    print(f"\n===== 🌑 TURNO {turno} =====")
    print("👾 MENÚ DE ATAQUE")
    print("1. Dante (Devil Hunter)")
    print("2. Alucard (Vampire Noble)")
    print("3. Igris (Black Knight)")
    print("4. Bell (White Rabbit)")
    print("5. Ver salud del Abismo")
    print("6. Salir")

    try:
        opcion = int(input("Elige un personaje para atacar al abismo: "))

        if opcion == 1:
            if cazador.esta_vivo():
                # Golpe crítico en el turno 3
                if turno == 3:
                    print("💥 ¡Golpe crítico de Dante! +500 fuerza extra")
                    cazador.fuerza += 500
                cazador.atacar(abismo)
            else:
                print(f"{cazador.nombre} está fuera de combate.")

        elif opcion == 2:
            if vampiro.esta_vivo():
                if turno == 3:
                    print("💥 ¡Golpe crítico de Alucard! +500 fuerza extra")
                    vampiro.fuerza += 500
                vampiro.atacar(abismo)
            else:
                print(f"{vampiro.nombre} está fuera de combate.")

        elif opcion == 3:
            if caballero.esta_vivo():
                if turno == 3:
                    print("💥 ¡Golpe crítico de Igris! +500 fuerza extra")
                    caballero.fuerza += 500
                caballero.atacar(abismo)
            else:
                print(f"{caballero.nombre} está fuera de combate.")

        elif opcion == 4:
            if conejo.esta_vivo():
                if turno == 3:
                    print("💥 ¡Golpe crítico de Bell! +500 fuerza extra")
                    conejo.fuerza += 500
                conejo.atacar(abismo)
            else:
                print(f"{conejo.nombre} está fuera de combate.")

        elif opcion == 5:
            abismo.mostrar_personaje()

        elif opcion == 6:
            print("👋 ¡Hasta la próxima!")
            break

        else:
            print("❌ Opción no válida.")

        # Ver si el abismo fue derrotado
        if abismo.salud <= 0:
            print("\n✨ ¡El Abismo ha sido derrotado! ¡Victoria para los héroes!")
            break

        # Abismo contraataca
        vivos = [p for p in heroes if p.esta_vivo()]
        if vivos:
            objetivo = random.choice(vivos)
            abismo.atacar_jugador(objetivo)
        else:
            print("\n⚰️ Todos los personajes han sido derrotados. El Abismo gana.")
            break

        turno += 1  # Incrementar turno después del ataque

    except ValueError:
        print("❌ Ingresa solo números válidos.")