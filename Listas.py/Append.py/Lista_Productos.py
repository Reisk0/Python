# Creamos una lista vacía donde se guardarán los productos
canasta = []

# Iniciamos un bucle que continuará hasta que el usuario decida salir
while True:
    # Solicitamos al usuario que ingrese un producto y lo convertimos a minúsculas
    entrada = input("Ingresa un producto, se agregará a tu canasta: ").lower()
    
    # Agregamos el producto ingresado a la lista 'canasta'
    canasta.append(entrada)
    
    # Mostramos confirmación de que se agregó el producto
    print(f"Producto '{entrada}' agregado.")

    # Preguntamos qué desea hacer a continuación: agregar, eliminar o salir
    opciones = input("¿Deseas agregar otro producto, eliminar uno o salir? (agregar/eliminar/salir): ").lower()

    # Si elige "agregar", el bucle continúa para ingresar otro producto
    if opciones == "agregar":
        continue

    # Si elige "eliminar", le mostramos la lista y pedimos qué producto quiere quitar
    elif opciones == "eliminar":
        print(f"Productos en la canasta: {canasta}")
        eliminar = input("¿Qué producto deseas eliminar?: ").lower()
        
        # Verificamos si el producto está en la canasta
        if eliminar in canasta:
            # Si está, lo eliminamos
            canasta.remove(eliminar)
            print(f"Producto '{eliminar}' eliminado.")
        else:
            # Si no está, avisamos al usuario
            print(f"El producto '{eliminar}' no está en la canasta.")

    # Si elige "salir", terminamos el bucle
    elif opciones == "salir":
        break

    # Si ingresa una opción no válida, se lo notificamos
    else:
        print("Opción no reconocida, intenta de nuevo.")

# Cuando el bucle termina, mostramos la lista final de productos
print(f"\nLista final de productos: {canasta}")