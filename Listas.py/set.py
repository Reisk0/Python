

frutas = []
for i in range(5):
    entrada = input(f"Ingrese el nombre de la fruta {i+1}: ")
    frutas.append(entrada)

print("\nCinco frutas ingresadas:")
for fruta in frutas:
    print(f"- {fruta}")


animalesFiltrados = []

for i in range(5): 
    mascota = input("Ingresa un animal que no empiece con la letra P: ").lower()
    
    if mascota.startswith("p"):
        print("Animal inválido")
    else:
        animalesFiltrados.append(mascota)

print("\nAnimales válidos ingresados:", animalesFiltrados)

