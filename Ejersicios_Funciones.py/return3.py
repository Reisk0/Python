# Bucle que sigue pidiendo datos hasta que se ingresen correctamente
while True:
    try:
        # 1. Solicitamos al usuario que escriba 3 números separados por comas
        entrada = input("Ingresa largo, alto y ancho separados por comas (ej. 2,3,4): ")

        # 2. Usamos split para dividir el texto en 3 partes y map + float para convertirlas a números
        largo, alto, ancho = map(float, entrada.split(","))

        # 3. Si todo salió bien, salimos del bucle con break
        break

    except ValueError:
        # 4. Si hubo un error (como letras en lugar de números), mostramos un mensaje y se repite
        print("❌ Entrada inválida. Asegúrate de ingresar 3 números separados por comas.")

# 5. Definimos la función para calcular el volumen
def calcular_volumen(largo, alto, ancho):
    volumen = largo * alto * ancho
    return volumen

# 6. Llamamos la función con los valores ya verificados
resultado = calcular_volumen(largo, alto, ancho)

# 7. Mostramos el resultado
print(f"✅ El volumen de largo {largo}, alto {alto}, ancho {ancho} es: {resultado}")