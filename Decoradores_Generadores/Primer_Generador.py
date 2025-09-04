"""
🎯 Objetivo:
✅ Crear una función con yield
✅ Que genere pares: 0, 2, 4, 6, 8, 10, 12, 14, 16, 18
"""

# Definimos una función generadora llamada 'generar_pares'
def generar_pares():
    # Inicializamos una variable llamada 'numero' en 0
    numero = 0

    # Creamos un ciclo while que se ejecuta mientras 'numero' sea menor a 20
    while numero < 20:
        # 'yield' devuelve el valor actual de 'numero' y PAUSA la función
        # La próxima vez que se llame al generador, continuará desde aquí
        yield numero

        # Aumentamos 'numero' en 2 para generar solo números pares
        numero += 2

# Creamos una instancia del generador llamando a la función
pares = generar_pares()

# Imprimimos un título descriptivo antes de mostrar los resultados
print("Los números pares son:")

# Recorremos el generador 'pares' usando un bucle for
# Cada vez que se entra al ciclo, se llama automáticamente a 'next(pares)'
for num in pares:
    # Imprimimos el número par actual generado
    print(num)